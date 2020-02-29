import requests
import json

url =  'https://movie.douban.com/j/search_subjects?type=movie&tag=\
    %E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&sort=recommend&page_limit=20&page_start=20'

r = requests.get(url).content.decode('utf8')
res = json.loads(r)
print(res)
