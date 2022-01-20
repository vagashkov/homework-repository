import csv
import datetime
import json
import os
import time

import requests

# biulding url for GET request
base_url = "https://api.vk.com/method/"
method = "wall.get"
owner_id = "12446354"

# build parameters list for GET request
params = {}
posts_info = []


def read_token() -> str:
    access_token = open(os.getcwd() + "/" + "token_store.txt",
                        "r",
                        encoding="utf-8").readline()
    return access_token.strip()[1:]


# dict with params for wall.get request
params["access_token"] = read_token()
params["owner_id"] = "-" + owner_id
params["v"] = "5.131"
params["count"] = 1
params["offset"] = 0

# dicts with post statistics
posts_by_year = {}
posts_by_month = {}
posts_by_weekday = {}
posts_by_hour = {}


totals = {}
totals["likes"] = 0
totals["reposts"] = 0
totals["comments"] = 0


def get_json(url: str, params: dict = None):
    """ function receives URL of object to retrieve and returns
    its JSON desctription """
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()


def process_post_date(post_info):
    post_date = datetime.datetime.fromtimestamp(post_info)
    # update "posts by year" statistics
    if post_date.year in posts_by_year:
        posts_by_year[post_date.year] += 1
    else:
        posts_by_year[post_date.year] = 1
    # update "posts by month" statistic
    if post_date.month in posts_by_month:
        posts_by_month[post_date.month] += 1
    else:
        posts_by_month[post_date.month] = 1
    # update "posts by weekday" statistics
    if post_date.weekday() in posts_by_weekday:
        posts_by_weekday[post_date.weekday()] += 1
    else:
        posts_by_weekday[post_date.weekday()] = 1
    # update "posts by hour" statistics
    if post_date.hour in posts_by_hour:
        posts_by_hour[post_date.hour] += 1
    else:
        posts_by_hour[post_date.hour] = 1


def collect_post_info(post) -> list:
    # getting post info as list id, text, attachments, attachments number,
    # likes, reposts and comments number
    post_info = []
    post_info.append(str(post["id"]))  # post id
    post_info.append(post["text"])  # post test
    attachments = []
    # check if post has any attachments
    if "attachments" in post:
        attachments_info = post["attachments"]
        attachments = [attachment["type"] for attachment in attachments_info]
    post_info.append(",".join(attachments))  # attachment types (?)
    post_info.append(str(len(attachments)))  # number of attachments
    post_info.append(str(post["likes"]["count"]))  # number of likes
    post_info.append(str(post["reposts"]["count"]))  # number of reposts
    post_info.append(str(post["comments"]["count"]))  # number of comments
    # now update "totals" statistics
    global totals
    totals["likes"] += post["likes"]["count"]
    totals["reposts"] += post["reposts"]["count"]
    totals["comments"] += post["comments"]["count"]
    # and process date-based statistics
    process_post_date(post["date"])
    return post_info


def generate_wall_report():
    # getting wall content as JSON-formatted text
    wall_content = get_json(base_url + method, params)
    # getting total number of posts
    posts_count = wall_content["response"]["count"]
    # setting initial parameters
    counter = 0
    params["count"] = 100
    # create CSV file for report
    with open(os.getcwd() + "/" + owner_id + ".csv",
              "w") as file:
        # create writer object
        csv_writer = csv.writer(file, delimiter=";", quotechar='"',
                                quoting=csv.QUOTE_MINIMAL)
        # first row will contain column headers
        csv_writer.writerow(("id", "text", "attachments", "attachments_count",
                             "likes_count", "reposts_count", "comments_count"))
        # walking through all the posts by 100 posts-sized chunks
        while counter < posts_count:
            # define offset for current wall part
            params["offset"] = counter
            # getting its content
            page_content = get_json(base_url + method, params)
            # and list of its post objects
            posts = page_content["response"]["items"]
            for post in posts:
                # collecting current post description
                post_info = collect_post_info(post)
                # and flush it into CSV-file
                csv_writer.writerow((post_info[:-1]))
            # "moving window" of current wall part
            counter += 100
            # make a pause to avoid ban from data source
            time.sleep(0.5)


def get_posts_stats():
    """ putting posts statistics into JSON file """
    with open(os.getcwd() + f"/{owner_id}_posts_stats.txt",
              "w") as file:
        posts_statistics = {"by_year": sorted(posts_by_year.items()),
                            "by_month": sorted(posts_by_month.items()),
                            "by_weekday": sorted(posts_by_weekday.items()),
                            "by_hour": sorted(posts_by_hour.items())}
        json.dump(posts_statistics, file)


def get_other_stats():
    """ putting likes, reposts and comments statistics
    into another JSON file """
    with open(os.getcwd() + f"/{owner_id}_other_stats.txt",
              "w") as file:
        likes_statistics = {
            "by_year": totals["likes"]/len(posts_by_year.items()),
            "by_month": totals["likes"]/12,
            "by_weekday": totals["likes"]/7,
            "by_hour": totals["likes"]/24}
        reposts_statistics = {
            "by_year": totals["reposts"]/len(posts_by_year.items()),
            "by_month": totals["reposts"]/12,
            "by_weekday": totals["reposts"]/7,
            "by_hour": totals["reposts"]/24}
        comments_statistics = {
            "by_year": totals["comments"]/len(posts_by_year.items()),
            "by_month": totals["comments"]/12,
            "by_weekday": totals["comments"]/7,
            "by_hour": totals["comments"]/24}
        other_statistics = {
            "likes": likes_statistics,
            "reposts": reposts_statistics,
            "comments": comments_statistics}
        json.dump(other_statistics, file)


if __name__ == "__main__":
    generate_wall_report()
    get_posts_stats()
    get_other_stats()
