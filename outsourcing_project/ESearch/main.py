from scrapy.cmdline import execute
import sys
import os


# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# execute(["scrapy","crawl","qcenglish"])
# execute(["scrapy","crawl","sina"])
# execute(["scrapy","crawl","Readfree"])
# execute(["scrapy","crawl","kankandou"])


from scrapy import cmdline
# cmdline.execute("scrapy crawl haoyang".split())
# cmdline.execute("scrapy crawl cenpub".split())
# cmdline.execute("scrapy crawl xiaomuchong".split())
# cmdline.execute("scrapy crawl zhangshang".split())
# cmdline.execute("scrapy crawl zoudupai".split())
# cmdline.execute("scrapy crawl chaoxing ".split())
# cmdline.execute("scrapy crawl qidian ".split())
# cmdline.execute("scrapy crawl ruochu ".split())
# cmdline.execute("scrapy crawl qwsy".split())
# cmdline.execute("scrapy crawl shuhai".split())
cmdline.execute("scrapy crawl zongheng".split())

