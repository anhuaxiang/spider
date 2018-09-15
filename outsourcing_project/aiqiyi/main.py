from scrapy import cmdline
# cmdline.execute("scrapy crawl aiqiyi -o aiqiyi_movie_info.csv ".split())
cmdline.execute("scrapy crawl comment -o aiqiyi_comment.csv ".split())