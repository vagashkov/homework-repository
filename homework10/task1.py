import asyncio
import json
import os
import urllib.request
import xml.etree.ElementTree as ET

import aiohttp
from bs4 import BeautifulSoup


class Company:
    """ class to store (for now) company data"""
    def __init__(self, name):
        self.name = name
        self.code = ""
        self.cur_price_usd = 0
        self.year_high = 0
        self.year_low = 0
        self.year_results = 0
        self.pe_ratio = 0


# list with all the company objects
allCompanies = []
# base url to retrieve data
base_url = "https://markets.businessinsider.com"


def extract_value(tag_string):
    """ extracts float value from given tag text"""
    return float(tag_string.strip().split()[0].replace(",", ""))


def get_usd_rate():
    """ extracts current USD rate from CB site """
    # getting central bank rates page content
    info_url = r"https://www.cbr.ru/scripts/XML_daily.asp"
    page = urllib.request.urlopen(info_url).read()
    # and parsing it
    root = ET.fromstring(page)
    # looking for 840 (USD) currency node
    for rate in root:
        if rate.find("NumCode").text == "840":
            return float(rate.find("Value").text.replace(",", "."))


def build_companies_list(base_url: str):
    """ function to build initial list of
    company objects """
    for pageNumber in range(1, 20):
        # building url using simple pattern
        url = base_url + r"/index/components/s&p_500?p="+str(pageNumber)
        # reading current page
        page = urllib.request.urlopen(url).read().decode()
        # and parsing it
        main_page_info = BeautifulSoup(page, "html.parser")
        # company info are located in table rows
        # and each row begins with specified class cell
        companiesList = main_page_info.findAll('td', class_='table__td--big')
        # checking if we still have some info to process
        if not len(companiesList):
            break
        # walking table row by row
        for company in companiesList:
            # getting href element containig company name
            link = company.find("a")
            if link and link.text:
                # we got some - build new Company class instance
                company_object = Company(link.text)
                company_object.link = link["href"]
                # getting the full company info row
                company_info = company.find_parent("tr")
                if company_info:
                    # getting the latest price first
                    latest_prices = company_info.find_all("td")[1]
                    if latest_prices:
                        cur_price = latest_prices.text.split()[0]
                        # and storing result in object
                        company_object.cur_price_usd = extract_value(cur_price)
                    # now browse to the last column
                    year_results = company_info.find_all("td")[7]
                    # extracting company year results
                    if year_results:
                        result_prc = year_results.find_all("span")[1].text
                        # and storing result in percent
                        company_object.year_results = float(result_prc[:-1])
                # finally append our new company to list
                allCompanies.append(company_object)


async def fetch_details(company_object, session):
    """ async function to fill company objects with all
    necessary info from company pages"""
    try:
        async with session.get(base_url + company_object.link) as response:
            # getting company page content
            company_page = await response.read()
            # and parsing it
            page_info = BeautifulSoup(company_page, "html.parser")
            # looking for company ticket code
            ticket = page_info.find('span', class_='price-section__category')
            if ticket:
                company_object.code = ticket.text.split(",")[1].strip()
            # now let's find company 52 weeks high and low
            # high-low section can contain different types
            # of high-low indicators (daily, weekly etc)
            high_low = page_info.find("div",
                                      class_="snapshot__highlow-container")
            high_low_items = page_info.find_all("div",
                                                class_="snapshot__highlow")
            # looking for year high-low info
            for high_low_item in high_low_items:
                key = "snapshot__data-item"
                scores = high_low_item.find_all("div",
                                                class_=key)
                for score in scores:
                    key = "snapshot__header"
                    score_type = score.find("div", class_=key)
                    # we are in year hish-low section
                    if score_type and score_type.text == "52 Week Low":
                        company_object.year_low = extract_value(score.text)
                    elif score_type and score_type.text == "52 Week High":
                        company_object.year_high = extract_value(score.text)
            # now browse to parent tag
            company_snapshot = high_low.find_parent("div")
            if company_snapshot:
                key = "snapshot__data-item"
                # browsing through all the company snapshot info
                # in order to find P/E ration (it can be in different places)
                snapshot_values = company_snapshot.find_all("div", class_=key)
                for value in snapshot_values:
                    key = "snapshot__header"
                    if value.find("div", class_=key).text == r"P/E Ratio":
                        company_object.pe_ratio = extract_value(value.text)
            return ('OK')
    except Exception as e:
        print(e)
        return (company_object.link, 'ERROR', str(e))


async def run(companies_list):
    """ function to start company info retrueving
    process and collect results """
    tasks = []
    async with aiohttp.ClientSession() as session:
        # we use company object as
        # parallelization base
        for company in companies_list:
            task = asyncio.ensure_future(fetch_details(company, session))
            tasks.append(task)
        responses = asyncio.gather(*tasks)
        await responses
    return responses


def build_data():
    """ function to gather and analize all the data"""
    build_companies_list(base_url)
    try:
        asyncio.run(run(allCompanies))
    except RuntimeError as ex:
        print(ex)

    # getting top-10 companies by stock price
    usd_rate = get_usd_rate()
    top_priced = sorted(allCompanies,
                        key=lambda x: x.cur_price_usd, reverse=True)[:10]
    # and put it into file in JSON format
    with open(os.getcwd() + r"/homework10/price_winners.txt",
              "w") as price_winners:
        for winner in top_priced:
            json_dict = {}
            json_dict["name"] = winner.name
            json_dict["code"] = winner.code
            json_dict["price"] = winner.cur_price_usd * usd_rate
            json.dump(json_dict, price_winners)

    # getting top-10 companies with lowest P/E ratio
    lowest_pe = sorted(allCompanies,
                       key=lambda x: x.pe_ratio)[:10]
    with open(os.getcwd() + r"/homework10/pe_winners.txt",
              "w") as pe_winners:
        for winner in lowest_pe:
            json_dict = {}
            json_dict["name"] = winner.name
            json_dict["code"] = winner.code
            json_dict["P//E"] = winner.pe_ratio
            json.dump(json_dict, pe_winners)

    # getting top-10 companies by annual growth
    top_growth = sorted(allCompanies,
                        key=lambda x: x.year_results, reverse=True)[:10]
    with open(os.getcwd() + r"/homework10/growth_winners.txt",
              "w") as growth_winners:
        for winner in top_growth:
            json_dict = {}
            json_dict["name"] = winner.name
            json_dict["code"] = winner.code
            json_dict["growth"] = winner.year_results
            json.dump(json_dict, growth_winners)

    # getting top-10 top bargain (for individual stock)
    top_bargain = sorted(allCompanies,
                         key=lambda x: x.year_high-x.year_low,
                         reverse=True)[:10]
    with open(os.getcwd() + r"/homework10/bargain_winners.txt",
              "w") as bargain_winners:
        for winner in top_bargain:
            json_dict = {}
            json_dict["name"] = winner.name
            json_dict["code"] = winner.code
            json_dict["potential profit"] = winner.year_high - winner.year_low
            json.dump(json_dict, bargain_winners)
