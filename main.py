import libCore.feed_class as feed
import datetime
date_ = datetime.datetime.now()
feed_ = feed.feed()

count_number_article = feed_.pipe_extract_rss()

print(f"[{date_}] - Run complete with {count_number_article} new article !")