import datetime
import os
import time

import requests
from posts._base import Post


class VKPost(Post):
    """Class describes data and behaviour of single VK post."""
    # URL components for GET request.
    base_url = "https://api.vk.com/method/"
    method = "video.get"
    params = {"v": "5.131"}

    def read_token(self) -> str:
        """Function receives access token from specified text file."""
        access_token = open(os.getcwd() + "/" + "token_store.txt",
                            "r",
                            encoding="utf-8").readline()
        return access_token.strip()[1:]

    def get_json(self, url: str, method: str, params: dict = None):
        """Function retrieves JSON description of object specified by
        argument values."""
        response = requests.get(url+method, params=params)
        if response.status_code == 200:
            return response.json()

    def get_photo_url(self, photo_desc: str) -> str:
        attachment_url = ""
        allowed_sizes = ["w", "z", "y", "x", "r", "q", "p", "o", "m", "s"]
        photo_sizes = photo_desc["sizes"]
        biggest_size_position = len(allowed_sizes) - 1
        for size in photo_sizes:
            type_position = allowed_sizes.index(size["type"])
            if type_position < biggest_size_position:
                attachment_url = size["url"]
                biggest_size_position = type_position
        return attachment_url

    def get_album_url(self, album_desc: str) -> str:
        attachment_url = ""
        allowed_sizes = ["w", "z", "y", "x", "r", "q", "p", "o", "m", "s"]
        album_sizes = album_desc["thumb"]["sizes"]
        biggest_size_position = len(allowed_sizes) - 1
        for size in album_sizes:
            type_position = allowed_sizes.index(size["type"])
            if type_position < biggest_size_position:
                attachment_url = size["url"]
                biggest_size_position = type_position
        return attachment_url

    def get_poll_url(self, poll_desc: str) -> str:
        return "Poll " + str(poll_desc["id"])

    def get_event_url(self, event_desc: str) -> str:
        return "Event " + str(event_desc["id"])

    def get_video_url(self, video_desc: str) -> str:
        time.sleep(0.3)
        params = {}
        params["v"] = self.params["v"]
        params["videos"] = "_".join((str(video_desc["owner_id"]),
                                     str(video_desc["id"]),
                                     video_desc["access_key"]))
        params["access_token"] = self.read_token()
        # Now try to load video content
        response = self.get_json(self.base_url, self.method, self.params)
        if "response" in response:
            response = response["response"]
        if "items" in response:
            response = response["items"][0]
        return response.get("player", "content_restricted")

    def __init__(self, post: str):
        """Function initializes single VK post object
        with values stored in post_content in JSON format."""
        self.id = post["id"]  # Post own id
        self.text = post["text"]  # Post text
        # Post creation date
        self.date = datetime.datetime.fromtimestamp(post["date"])
        # Number of likes
        self.likes_count = post["likes"]["count"]
        # Number of reposts
        self.reposts_count = post["reposts"]["count"]
        # Number of comments
        self.comments_count = post["comments"]["count"]
        self.attachment_urls = []
        self.attachments_count = 0
        # Check if post has any attachments
        if "attachments" in post:
            attachments_list = post["attachments"]
            for attachment in attachments_list:
                attachment_type = attachment["type"]
                attachment_object = attachment[attachment_type]
                attachment_url = ""
                if "url" in attachment_object:
                    attachment_url = attachment_object["url"]
                elif attachment_type == "photo":
                    attachment_url = self.get_photo_url(attachment_object)
                elif attachment_type == "video":
                    attachment_url = self.get_video_url(attachment_object)
                elif attachment_type == "poll":
                    attachment_url = self.get_poll_url(attachment_object)
                elif attachment_type == "event":
                    attachment_url = self.get_event_url(attachment_object)
                elif attachment_type == "album":
                    attachment_url = self.get_album_url(attachment_object)
                if not attachment_url:
                    print(attachment_type)
                    attachment_url = attachment_type
                self.attachment_urls.append(attachment_url)
        self.attachments_count = len(self.attachment_urls)
        self.attachments = ",".join(self.attachment_urls)

    def to_csv(self, fields_list: list):
        """Function returns CSV-formatted description of object."""
        csv_list = [str(getattr(self, field_name))
                    for field_name in fields_list]
        return csv_list
        """(str(self.id),
        self.text,
        self_fields_list),
        str(len(self.attachments)),
        str(self.likes_count),
        str(self.reposts_count),
        str(self.comments_count),)"""
