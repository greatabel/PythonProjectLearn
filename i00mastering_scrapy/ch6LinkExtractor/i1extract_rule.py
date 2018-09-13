from scrapy.http import HtmlResponse
import mycolor


html1 = open('example1.html').read()
html2 = open('example2.html').read()
response1 = HtmlResponse(url='http://example1.com', body=html1, encoding='utf8')
response2 = HtmlResponse(url='http://example2.com', body=html2, encoding='utf8')


from scrapy.linkextractors import LinkExtractor
le = LinkExtractor()
links = le.extract_links(response1)
for link in links:
    print(link)

print(mycolor.show('allow 参数 --------'))
pattern = '/intro/.+\.html$'
le = LinkExtractor(allow=pattern)
links = le.extract_links(response1)
for link in links:
    print(link)