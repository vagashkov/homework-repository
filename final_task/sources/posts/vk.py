﻿import datetime
import os
import time

import requests

from ._base import Post


class VKPost(Post):
    """Class describes data and behaviour of single VK post."""

    # Define some 'constants' for current source:
    # Current API version
    API_VERSION = os.getenv("VK_API_VERSION")
    if not API_VERSION:
        API_VERSION = "5.131"
    # Minimum time between request to avoid locking
    PAUSE_LENGTH = os.getenv("VK_PAUSE_LENGTH")
    if not PAUSE_LENGTH:
        PAUSE_LENGTH = 0.4

    # URL components for GET request.
    base_url = "https://api.vk.com/method/"
    method = "video.get"
    params = {"v": API_VERSION}

    def __init__(self, post: str):
        """Function initializes single VK post object
        with values stored in post_content in JSON format."""
        self.id = post.get("id", 0)  # Post own id
        self.text = post.get("text", "")  # Post text
        # Post creation date
        self.date = datetime.datetime.fromtimestamp(post.get("date", ""))
        # Number of likes
        self.likes_count = post.get("likes", {}).get("count", 0)
        # Number of reposts
        self.reposts_count = post.get("reposts", {}).get("count", 0)
        # Number of comments
        self.comments_count = post.get("comments", {}).get("count", 0)
        self.attachment_urls = []
        self.attachments_count = 0
        # Check if post has any attachments
        if "attachments" in post:
            attachments_list = post.get("attachments", [])
            for attachment in attachments_list:
                attachment_type = attachment.get("type", "")
                attachment_object = attachment.get(attachment_type, {})
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
                    attachment_url = attachment_type
                self.attachment_urls.append(attachment_url)
        self.attachments_count = len(self.attachment_urls)
        self.attachments = ",".join(self.attachment_urls)

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
            type_position = allowed_sizes.index(size.get("type", ""))
            if type_position < biggest_size_position:
                attachment_url = size.get("url", 0)
                biggest_size_position = type_position
        return attachment_url

    def get_album_url(self, album_desc: str) -> str:
        attachment_url = ""
        allowed_sizes = ["w", "z", "y", "x", "r", "q", "p", "o", "m", "s"]
        album_sizes = album_desc.get("thumb", {}).get("sizes", {})
        biggest_size_position = len(allowed_sizes) - 1
        for size in album_sizes:
            type_position = allowed_sizes.index(size.get("type", ""))
            if type_position < biggest_size_position:
                attachment_url = size.get("url", "")
                biggest_size_position = type_position
        return attachment_url

    def get_poll_url(self, poll_desc: str) -> str:
        return "Poll " + str(poll_desc.get("id", 0))

    def get_event_url(self, event_desc: str) -> str:
        return "Event " + str(event_desc.get("id", 0))

    def get_video_url(self, video_desc: str) -> str:
        time.sleep(self.PAUSE_LENGTH)
        params = {}
        params["v"] = self.params["v"]
        params["videos"] = "_".join((str(video_desc.get("owner_id", "")),
                                     str(video_desc.get("id", 0)),
                                     video_desc["access_key"]))
        params["access_token"] = os.getenv("ACCESS_TOKEN")
        # Now try to load video content
        response = self.get_json(self.base_url, self.method, self.params)
        if "response" in response:
            response = response["response"]
        if "items" in response:
            response = response.get("items", [])[0]
        return response.get("player", "content_restricted")

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
