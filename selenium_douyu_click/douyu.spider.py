# -*- coding:utf-8 -*-

from selenium import webdriver
from bs4 import BeautifulSoup as bs


class Douyu:
    def __init__(self):
        self.driver = webdriver.PhantomJS()
        # self.driver = webdriver.Chrome()
        self.num = 0
        self.count = 0

    def douyu_pider(self):
        self.driver.get("https://www.douyu.com/directory/all")
        while True:
            soup = bs(self.driver.page_source, "lxml")
            # 房间名, 返回列表
            names = soup.find_all("span", {"class": "dy-name ellipsis fl"})
            # 观众人数, 返回列表
            numbers = soup.find_all("span", {"class": "dy-num fr"})

            for name, number in zip(names, numbers):
                print(u"观众人数: -" + number.get_text().strip() + u"-\t房间名: " + name.get_text().strip())
                self.num += 1
                count = number.get_text().strip()
                if count[-1] == "万":
                    countNum = float(count[:-1]) * 10000
                else:
                    countNum = float(count)
                self.count += countNum

            # 一直点击下一页
            self.driver.find_element_by_class_name("shark-pager-next").click()
            # 如果在页面源码里找到"下一页"为隐藏的标签，就退出循环
            if self.driver.page_source.find("shark-pager-disable-next") != -1:
                break

        print("当前网站直播人数:%s" % self.num)
        print("当前网站观众人数:%s" % self.count)


if __name__ == "__main__":
    d = Douyu()
    d.douyu_pider()
