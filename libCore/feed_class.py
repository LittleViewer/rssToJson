import json
import lib.utils_class as utils
import feedparser

class feed:



    def extract_feed_link(self, link):
        
        if self.utils_.check_file_exist(link):
            handle = self.utils_.file_open(link)
            json.load(handle)
        else:
            self.utils_.stop_with_reason("Bad File Path of RSS Feed")

    def pipe_extract_rss(self, link = "configFolder\\rssFeed.json"):
        self.extract_feed_link(link)

    def __init__(self):
        self.utils_ = utils.util()