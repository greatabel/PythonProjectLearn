import scrapy

class BooksSpider(scrapy.Spider):

    name = 'books'

    start_urls = ['http://books.toscrape.com/']
    