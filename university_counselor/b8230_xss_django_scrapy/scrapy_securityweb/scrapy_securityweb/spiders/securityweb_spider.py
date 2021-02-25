import scrapy
from scrapy.selector import Selector

'''
python3 -m scrapy crawl securityweb 
python3 -m scrapy crawl securityweb -o securitywebs.json

'''

class SecurityWebSpider(scrapy.Spider):

    def __init__(self):
        self.page_index = 1


    name = 'securityweb'
    start_urls = ['http://hackernews.cc/']
    # start_urls = ['https://www.cert.org.cn/publish/main/12/index.html']
    # start_urls = ['http://books.toscrape.com/']
    def parse(self, response):
        # hxs = Selector(response=response).xpath('//a') #标签对象列表
        # for sel in hxs:
        #     myname = sel.xpath('//a/text()').extract()
        #     mylink = sel.xpath('//a/@href').extract()
        #     print(myname, '#'*10, mylink)
        items = '.classic-list-title a'

        for i in response.css(items):
            title = i.css('::text').extract_first()
            link = i.css('::attr(href)').extract_first()
            # yield dict(title=title, title_link=link)
            print(title, link, '#'*5)
            yield {'title': title, 'link': link}

        # for book in response.css('classic-list'):
        #     name = book.css('classic-list-title a::attr(href)').extract_first()
        #     price = book.css('light-post-meta').extract_first()
        #     print('#'*20, name, price)
        #     yield {'name': name, 'price': price}

        # https://blog.csdn.net/webfullstack/article/details/104878396
        self.page_index += 1
        # next_url = response.css('pagination clearfix a::attr(href)').extract_first()
        next_url = 'http://hackernews.cc/page/' + str(self.page_index)
        # next_url = response.xpath(PAGER_SELECTOR).extract_first()
        print('>'*10, next_url)
        if next_url and self.page_index <= 2:
            # 如果找到下一页的URL，得到绝对路径，构造新的Request 对象
            next_url = response.urljoin(next_url)
            yield scrapy.Request(next_url, callback=self.parse)




