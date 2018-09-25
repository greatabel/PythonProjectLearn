scrapy shell http://matplotlib.org/examples/index.html

# ----
view(response)

from scrapy.linkextractors import LinkExtractor
le = LinkExtractor(restrict_css='div.toctree-wrapper.compound li.toctree-l2')
links = le.extract_links(response)
[link.url for link in links]

