import csv
import json
import os
import time
from datetime import datetime

import requests
from posts.vk import VKPost
from sources._base import Source


class VKSource(Source):
    """Class uses VK wall as data source."""
    required_parameters = ("owner_id, access_token, v,")
    available_fields = ["id", "text", "attachments", "attachments_count",
                        "likes_count", "reposts_count", "comments_count"]

    # URL components for GET request.
    base_url = "https://api.vk.com/method/"
    method = "wall.get"

    def get_json(self, url: str, method: str, params: dict = None):
        """Function retrieves JSON description of object specified by
        argument values."""
        response = requests.get(url+method, params=params)
        if response.status_code == 200:
            return response.json()

    def __init__(self, owner_id: str,
                 start_date=None,
                 fields_list=available_fields,
                 v: str = "5.131",
                 access_token: str = None):
        """Function initializes new VKSource instance and stores """
        # Initialize required parameter to perform request
        self.owner_id = owner_id
        self.start_date = start_date
        self.fields_list = fields_list
        self.v = v
        self.access_token = access_token
        if not self.access_token:
            self.access_token = os.getenv("ACCESS_TOKEN")

        # Initialize dict to store statistics for posts, likes etc.
        self.totals = {
            "posts": 0,
            "likes": 0,
            "reposts": 0,
            "comments": 0}

        # Initialize dicts with post statistics
        self.posts_by_year = {}
        self.posts_by_month = {}
        self.posts_by_weekday = {}
        self.posts_by_hour = {}

        # Pack values into dict to use as request parameters
        self.params = {
            "access_token": self.access_token,
            "owner_id": "-" + self.owner_id,
            "v": v,
            "count": 1,
            "offset": 0}

        # Now try to load wall content and check number of posts
        response = self.get_json(self.base_url, self.method, self.params)
        if "response" in response:
            response = response["response"]
            if "count" in response:
                self.totals["posts"] = response["count"]
        else:
            # Raise an exception if something went wrong
            pass

    def update_posts_statistics(self, post_date):
        """Function updates VKSource object posts statistics
        using current post publication date."""
        # Update "posts by year" statistics
        if post_date.year in self.posts_by_year:
            self.posts_by_year[post_date.year] += 1
        else:
            self.posts_by_year[post_date.year] = 1
        # Update "posts by month" statistic
        if post_date.month in self.posts_by_month:
            self.posts_by_month[post_date.month] += 1
        else:
            self.posts_by_month[post_date.month] = 1
        # Update "posts by weekday" statistics
        if post_date.weekday() in self.posts_by_weekday:
            self.posts_by_weekday[post_date.weekday()] += 1
        else:
            self.posts_by_weekday[post_date.weekday()] = 1
        # Update "posts by hour" statistics
        if post_date.hour in self.posts_by_hour:
            self.posts_by_hour[post_date.hour] += 1
        else:
            self.posts_by_hour[post_date.hour] = 1

    def update_totals(self, post):
        """Function updates VKSource object likes, posts and
        repost statistics using current post data."""
        self.totals["likes"] += post.likes_count
        self.totals["reposts"] += post.reposts_count
        self.totals["comments"] += post.comments_count

    def process_wall_content(self, file_name: str, file_format: str = "CSV"):
        """Function downloads wall by chunks, processes post data and
        stores it into CSV file."""
        # Setting initial parameters
        after_start_date = True
        post_counter = 0
        self.params["count"] = 100
        # Create and fill CSV file for report
        with open(file_name, "w") as file:
            # Create writer object for opened file
            csv_writer = csv.writer(
                       file,
                       delimiter=",",
                       quotechar='"',
                       quoting=csv.QUOTE_MINIMAL)
            # Write column headers into first row
            csv_writer.writerow(self.fields_list)
            # Walking through all the posts by 100 posts-sized chunks
            while post_counter < self.totals["posts"] and after_start_date:
                # Define offset for current wall fragment
                self.params["offset"] = post_counter
                # Getting wall fragment content
                page_content = self.get_json(self.base_url,
                                             self.method,
                                             self.params)
                # And list of its post objects
                posts = page_content["response"]["items"]
                for post_description in posts:
                    # Check if start date is defined
                    if self.start_date:
                        date_desc = post_description["date"]
                        post_date = datetime.fromtimestamp(date_desc).date()
                        if post_date < self.start_date:
                            after_start_date = False
                            continue
                    # Collecting current post description
                    post = VKPost(post_description)
                    # Update totals and post statictic with current post info
                    self.update_totals(post)
                    self.update_posts_statistics(post.date)
                    # And flush it into CSV-file
                    csv_writer.writerow(post.to_csv(self.fields_list))
                # Move "window" of current wall part
                post_counter += 100
                # Make a pause to avoid ban from data source
                time.sleep(0.5)

    def get_posts_statistics_html(self):
        """Function puts posts statistics into HTML table."""
        posts_statistics = {"Year": sorted(self.posts_by_year.items()),
                            "Month": sorted(self.posts_by_month.items()),
                            "Weekday": sorted(self.posts_by_weekday.items()),
                            "Hour": sorted(self.posts_by_hour.items())}
        tables = ""
        for statistic in posts_statistics:
            table = "<p><table border='1'>"
            table += f"<tr><th>{statistic}</th><th>Posts</th></tr>"
            for key, value in posts_statistics[statistic]:
                table += f"<tr><td>{key}</td><td>{value}</td></tr>"
            table += "</table>"
            tables += table
        return tables

    def get_posts_statistics(self, file_name: str):
        """Function puts posts statistics into specified JSON file."""
        with open(file_name, "w") as file:
            posts_statistics = {"by_year": self.posts_by_year,
                                "by_month": self.posts_by_month,
                                "by_weekday": self.posts_by_weekday,
                                "by_hour": self.posts_by_hour}
            return posts_statistics
            json.dump(posts_statistics, file)

    def get_other_statistics(self, file_name: str):
        """Function puts details posts statistics
        (likes, reposts and comments) into specified JSON file."""
        with open(file_name, "w") as file:
            year_num = len(self.posts_by_year.items())
            likes_statistics = {
                "by_year": self.totals["likes"]/year_num,
                "by_month": self.totals["likes"]/12,
                "by_weekday": self.totals["likes"]/7,
                "by_hour": self.totals["likes"]/24}
            reposts_statistics = {
                "by_year": self.totals["reposts"]/year_num,
                "by_month": self.totals["reposts"]/12,
                "by_weekday": self.totals["reposts"]/7,
                "by_hour": self.totals["reposts"]/24}
            comments_statistics = {
                "by_year": self.totals["comments"]/year_num,
                "by_month": self.totals["comments"]/12,
                "by_weekday": self.totals["comments"]/7,
                "by_hour": self.totals["comments"]/24}
            other_statistics = {
                "likes": likes_statistics,
                "reposts": reposts_statistics,
                "comments": comments_statistics}
            json.dump(other_statistics, file)

    def get_other_statistics_html(self, file_name: str = None):
        """Function puts details posts statistics
        (likes, reposts and comments) into HTML table. """
        year_num = len(self.posts_by_year.items())
        likes_statistics = {
            "Year": round(self.totals["likes"]/year_num, 2),
            "Month": round(self.totals["likes"]/12, 2),
            "Weekday": round(self.totals["likes"]/7, 2),
            "Hour": round(self.totals["likes"]/24, 2)}
        reposts_statistics = {
            "Year": round(self.totals["reposts"]/year_num, 2),
            "Month": round(self.totals["reposts"]/12, 2),
            "Weekday": round(self.totals["reposts"]/7, 2),
            "Hour": round(self.totals["reposts"]/24, 2)}
        comments_statistics = {
            "Year": round(self.totals["comments"]/year_num, 2),
            "Month": round(self.totals["comments"]/12, 2),
            "Weekday": round(self.totals["comments"]/7, 2),
            "Hour": round(self.totals["comments"]/24, 2)}

        # Collect all statistics into single dict to process
        statistics = {
            "Likes": likes_statistics,
            "Reposts": reposts_statistics,
            "Comments": comments_statistics}

        # Build tables based on dict data
        tables = ""
        for statistic in statistics.keys():
            cur_stat = statistics[statistic]
            print(cur_stat)
            table = f"<p><table border='1'><tr><th>{statistic}</th>"
            table += "<th>Number</th></tr>"
            for key in cur_stat.keys():
                table += f"<tr><td>{key}</td><td>{cur_stat[key]}</td></tr>"
            table += "</table>"
            tables += table
        return tables
