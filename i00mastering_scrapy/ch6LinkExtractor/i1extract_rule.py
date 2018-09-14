from scrapy.http import HtmlResponse
from scrapy.linkextractors import LinkExtractor
from urllib.parse import urlparse
import mycolor


html1 = open('example1.html').read()
html2 = open('example2.html').read()
response1 = HtmlResponse(url='http://example1.com', body=html1, encoding='utf8')
response2 = HtmlResponse(url='http://example2.com', body=html2, encoding='utf8')



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

print(mycolor.show('deny 参数 --------'))
print('“示例　提取页面example1.html中所有站外链接（即排除站内链接）”')
pattern1 = pattern1 = '^' + urlparse(response1.url).geturl()
print(pattern1)
le = LinkExtractor(deny=pattern1)
links = le.extract_links(response1)
for link in links:
    print(link)

print(mycolor.show('allow_domain 参数 --------'))
domains = ['github.com', 'stackoverflow.com']
le = LinkExtractor(allow_domains=domains)
links = le.extract_links(response1)
for link in links:
    print(link)

print(mycolor.show('deny_domain 参数 --------'))
domains = ['github.com', 'stackoverflow.com']
le = LinkExtractor(deny_domains=domains)
links = le.extract_links(response1)
for link in links:
    print(link)

print(mycolor.show('restrict_xpaths 参数 --------', 'blue'))
le = LinkExtractor(restrict_xpaths='//div[@id="top"]')
links = le.extract_links(response1)
for link in links:
    print(link)

print(mycolor.show('restrict_css 参数 --------'))
le = LinkExtractor(restrict_css='div#bottom')
links = le.extract_links(response1)
for link in links:
    print(link)

print(mycolor.show('tags attrs 参数 --------'))
le = LinkExtractor(tags='script', attrs="src")
links = le.extract_links(response1)
for link in links:
    print(link)

print(mycolor.show('process_value 参数 --------', 'blue'))

import re
def process(value):
    m = re.search("javascript:goToPage\('(.*?)'", value)
    if m:
        value = m.group(1)
    return value


le = LinkExtractor(process_value=process)
links = le.extract_links(response2)
for link in links:
    print(link)




