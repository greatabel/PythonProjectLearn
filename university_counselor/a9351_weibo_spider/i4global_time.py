from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from lxml import etree
import os
import requests
import csv

# 创建一个无头浏览器对象
chrome_options = Options()
# 设置它为无框模式
chrome_options.add_argument("--headless")
# 如果在windows上运行需要加代码
chrome_options.add_argument("--disable-gpu")
browser = webdriver.Chrome(executable_path='/Users/greatabel/AbelProject/PythonProjectLearn/university_counselor/a9351_weibo_spider/chromedriver')

# 设置一个10秒的隐式等待
browser.implicitly_wait(10)
# 使用谷歌无头浏览器来加载动态js
def start_get(url, news_type):
    browser.get(url)
    sleep(1)
    # for one in range(30):
    for one in range(1):
        # 翻到页底
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        sleep(1)
    # 拿到页面源代码
    source = browser.page_source
    parse_page(url, source)


# 对新闻列表页面进行解析
def parse_page(url, html):
    # 创建etree对象
    tree = etree.HTML(html)
    new_lst = tree.xpath('//ul[@id="recommend"]//a')
    for one_new in new_lst:
        title = one_new.xpath(".//h4/text()")[0]
        link = url + one_new.xpath("./@href")[0]
        try:
            write_in(title, link, news_type)
        except Exception as e:
            print(e)


# 将其写入到文件
def write_in(title, link, news_type):
    alist = []
    print("开始写入新闻:{}".format(title))
    # response = requests.get(url=link)
    browser.get(link)
    sleep(1)
    # 再次翻页到底
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    # 拿到页面源代码
    source = browser.page_source
    tree = etree.HTML(source)

    alist.append(news_type)
    # title = title.replace('?', '')
    alist.append(title)

    con_link = link
    alist.append(con_link)

    content_lst = tree.xpath('//section[@data-type="rtext"]/p')
    con = ""
    if content_lst:
        for one_content in content_lst:
            if one_content.text:
                con = con + "\n" + one_content.text.strip()
        alist.append(con)

        # post_time_source = tree.xpath('//div[@class="left-t"]')[0].text

        post_time = tree.xpath('//div[@class="metadata-info"]//p[@class="time"]')[
            0
        ].text
        alist.append(post_time)

        post_source = tree.xpath(
            '//div[@class="metadata-info"]//span[@class="source"]//a'
        )
        if post_source:
            post_source = post_source[0].text
        else:
            post_source = tree.xpath(
                '//div[@class="metadata-info"]//span[@class="source"]//span'
            )[0].text
        alist.append(post_source)
        # 1. 创建文件对象
        f = open("环球网n.csv", "a+", encoding="utf-8", newline="")
        # 2. 基于文件对象构建 csv写入对象
        csv_writer = csv.writer(f)
        print(alist)
        csv_writer.writerow(alist)
        f.close()


if __name__ == "__main__":
    urls = [
        "https://world.huanqiu.com/",
        # "https://china.huanqiu.com/",
        # "https://mil.huanqiu.com/",
        # "https://finance.huanqiu.com/",
        # "https://sports.huanqiu.com/",
        # "https://ent.huanqiu.com/",
    ]
    i = 0
    news_types = ["国际", "国内", "军事", "财经", "体育", "娱乐"]
    for url in urls:
        # headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'}
        if not os.path.exists("new"):
            os.mkdir("new")
        news_type = news_types[i]
        start_get(url, news_type)
        i = i + 1
    browser.quit()
