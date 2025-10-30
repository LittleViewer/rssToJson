import json
import libCore.utils_class as utils
import feedparser

class feed:



    def extract_feed_link(self, link):
        dict_feed = {}
        if self.utils_.check_file_exist(link):
            handle = self.utils_.file_open(link)
            content = json.load(handle)
            tick = 0
            for only_one_content in content:
                obj_feed = feedparser.parse(only_one_content["rss_link"])
                dict_feed = self.utils_.order_dict(only_one_content["rss_link"], only_one_content["language"], dict_feed, tick)
                tick += 1
                #for one_article in obj_feed.entries:
                    #print(one_article.title)
            print(dict_feed)
                
        else:
            self.utils_.error_with_reason("Bad File Path of RSS Feed", True)

    def pipe_extract_rss(self, link = "configFolder\\rssFeed.json"):
        self.extract_feed_link(link)

    def __init__(self):
        self.utils_ = utils.util()