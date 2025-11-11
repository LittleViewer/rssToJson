import json
import libCore.utils_class as utils
import libCore.json_class as json_class
import feedparser

class feed:



    def extract_feed_link(self, link):
        dict_feed = {}
        if self.utils_.check_file_exist(link):
            handle = self.utils_.file_open(link)
            content = json.load(handle)
            tick = 0
            for only_one_content in content:
                dict_feed = self.utils_.order_dict(only_one_content["rss_link"], only_one_content["country"], dict_feed, tick)
                tick += 1
            return dict_feed                
        else:
            self.utils_.error_with_reason("Bad File Path of RSS Feed", True)
    
    def parse_rss(self, dict_feed):
        parsed_feed_list = {}
        list_key = list(dict_feed.keys())
        tick_feed = 0
        for one_key in list_key:
            parsed_feed_list[one_key] = []
            for one_feed in dict_feed[one_key]:
                tick_feed += 1
                print(f"Read: {one_feed} #{tick_feed}")
                parsed_feed_list[one_key].append(feedparser.parse(one_feed))
        return parsed_feed_list
                
    
    def formated_result(self, parsed_feed_list):
        index_list = list(parsed_feed_list.keys())
        formated_feed_list = {}
        tick = 0
        for one_key in index_list:
            formated_feed_list[one_key] = []
            one_feed = parsed_feed_list[one_key]
            for one_article in one_feed[0].entries :
                formated_feed_list[one_key].append([one_article.title, one_article.description, one_article.published, one_article.link])  
            tick += 1
        return formated_feed_list
    
    def pipe_extract_rss(self, link = "configFolder/rssFeed.json"):
        dict_feed = self.extract_feed_link(self.utils_.absolute_link(link))
        parsed_feed_list = self.parse_rss(dict_feed)
        formated_feed = self.formated_result(parsed_feed_list)
        return self.json_.pipe_output(formated_feed)


    def __init__(self):
         self.utils_ = utils.utils()
         self.json_ = json_class.jsons_utils()