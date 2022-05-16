from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Spider
from scrapy.http import Request

DOMAIN = "localhost:5000/home/"
# DOMAIN = 'localhost:8000/scp2/'

URL = "http://%s" % DOMAIN


class MySpider(Spider):
    name = DOMAIN
    allowed_domains = [DOMAIN]
    start_urls = [URL]

    def parse(self, response):
        le = (
            LinkExtractor()
        )  # empty for getting everything, check different options on documentation
        for link in le.extract_links(response):
            print(link)
            yield Request(link.url, callback=self.parse)
