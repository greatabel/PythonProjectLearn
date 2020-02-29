import requests

from scrapy.selector import Selector

splash_url = 'http://localhost:8050/render.html'
args = {'url': 'http://quotes.toscrape.com/js', 'timeout': 5, 'image': 0}
response = requests.get(splash_url, params=args)
sel = Selector(response)
sels = sel.css('div.quote span.text::text').extract() #提取所有名人名言
print(sels)

