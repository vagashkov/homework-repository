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


def extract_value(tag_value: str) -> float:
    """ extracts float value from given tag text"""
    return float(tag_value.strip().split()[0].replace(",", ""))


def get_usd_rate() -> float:
    """ function to extract current USD rate from CB site """
    # getting central bank rates page content
    info_url = r"https://www.cbr.ru/scripts/XML_daily.asp"
    page = urllib.request.urlopen(info_url).read()
    # and parsing it
    root = ET.fromstring(page)
    # looking for 840 (USD) currency node
    for rate in root:
        if rate.find("NumCode").text == "840":
            return float(rate.find("Value").text.replace(",", "."))


def fetch_company_base_info(company_object, company_info):
    """ function to fetch base company info (current price and
    year result) from main page """
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


def build_company(company_tag):
    """ function to build single company object and fill
    it with initial information from its tag on main page"""
    # getting href element containig company name
    link = company_tag.find("a")
    if link and link.text:
        # we got some - build new Company class instance
        company_object = Company(link.text)
        company_object.link = link["href"]
        # getting the full company info row on main page
        company_info = company_tag.find_parent("tr")
        if company_info:
            fetch_company_base_info(company_object, company_info)
        return company_object


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
            company_object = build_company(company)
            if company_object:
                allCompanies.append(company_object)


def fetch_company_PE_ratio(info_tag):
    """ function to fetch company P/E ratio """
    key = "snapshot__data-item"
    # browsing through all the company snapshot info
    # in order to find P/E ration (it can be in different places)
    snapshot_values = info_tag.find_all("div", class_=key)
    for value in snapshot_values:
        key = "snapshot__header"
        if value.find("div", class_=key).text == r"P/E Ratio":
            return(extract_value(value.text))
    # return 0 if there is no P/E info on company page
    return 0


def fetch_company_high_low(company_object, page_info):
    """ function to fetch company year highest and lowest
    stock prices """
    # high-low section can contain different types
    # of high-low indicators (daily, weekly etc)
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
            fetch_company_high_low(company_object, page_info)

            # now get P/E ratio
            high_low = page_info.find("div",
                                      class_="snapshot__highlow-container")
            company_snap = high_low.find_parent("div")
            if company_snap:
                company_object.pe_ratio = fetch_company_PE_ratio(company_snap)

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


def get_top_by_stock_price(count: int):
    """ function gets top n companies by current
    stock price and stores it into JSON file"""
    # we need current USD exchange rate
    usd_rate = get_usd_rate()
    # gettin companies list
    top_priced = sorted(allCompanies,
                        key=lambda x: x.cur_price_usd, reverse=True)[:count]
    # and put it into file in JSON format
    with open(os.getcwd() + r"/homework10/price_winners.txt",
              "w") as price_winners:
        for winner in top_priced:
            # bpreparing dict with necessary info
            json_dict = {}
            json_dict["name"] = winner.name
            json_dict["code"] = winner.code
            json_dict["price"] = winner.cur_price_usd * usd_rate
            # and store it into file
            json.dump(json_dict, price_winners)


def get_top_by_lowest_pe_ratio(count: int):
    """ function gets top n companies by lowest
    P/E ratio and stores it into JSON file"""
    lowest_pe = sorted(allCompanies,
                       key=lambda x: x.pe_ratio)[:count]
    with open(os.getcwd() + r"/homework10/pe_winners.txt",
              "w") as pe_winners:
        for winner in lowest_pe:
            json_dict = {}
            json_dict["name"] = winner.name
            json_dict["code"] = winner.code
            json_dict["P//E"] = winner.pe_ratio
            json.dump(json_dict, pe_winners)


def get_top_by_annual_growth(count: int):
    """ function gets top n companies by year
    growth and stores it into JSON file"""
    top_growth = sorted(allCompanies,
                        key=lambda x: x.year_results, reverse=True)[:count]
    with open(os.getcwd() + r"/homework10/growth_winners.txt",
              "w") as growth_winners:
        for winner in top_growth:
            json_dict = {}
            json_dict["name"] = winner.name
            json_dict["code"] = winner.code
            json_dict["growth"] = winner.year_results
            json.dump(json_dict, growth_winners)


def get_top_by_stock_bargain(count: int):
    """ function gets top n companies by individual
    stock price raise and stores it into JSON file"""
    top_bargain = sorted(allCompanies,
                         key=lambda x: x.year_high-x.year_low,
                         reverse=True)[:count]
    with open(os.getcwd() + r"/homework10/bargain_winners.txt",
              "w") as bargain_winners:
        for winner in top_bargain:
            json_dict = {}
            json_dict["name"] = winner.name
            json_dict["code"] = winner.code
            json_dict["potential profit"] = winner.year_high - winner.year_low
            json.dump(json_dict, bargain_winners)


def build_data():
    """ function to gather and analize all the data"""
    # building companies objects with initial data
    build_companies_list(base_url)

    # filling company objects with additional data
    try:
        asyncio.run(run(allCompanies))
    except RuntimeError as ex:
        print(ex)

    # getting top-10 companies by stock price
    get_top_by_stock_price(10)

    # getting top-10 companies with lowest P/E ratio
    get_top_by_lowest_pe_ratio(10)

    # getting top-10 companies by annual growth
    get_top_by_annual_growth(10)

    # getting top-10 top bargain (for individual stock)
    get_top_by_stock_bargain(10)
