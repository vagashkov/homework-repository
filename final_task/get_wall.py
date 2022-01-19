import csv
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


params["access_token"] = read_token()
params["owner_id"] = "-" + owner_id
params["v"] = "5.131"
params["count"] = 1
params["offset"] = 0


def get_json(url: str, params: dict = None):
    """ function receives URL of object to retrieve and returns
    its JSON desctription """
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()


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
                csv_writer.writerow((post_info))
            # "moving window" of current wall part
            counter += 100
            # make a pause to avoid ban from data source
            time.sleep(0.5)


if __name__ == "__main__":
    generate_wall_report()
