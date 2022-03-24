import json
import requests
from lxml import etree

data_folder = "data"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
}
response = requests.get("https://www.baidu.com/s?wd=中国共产党大事记2021&lm=2", headers=headers)


r = response.text
print("len(r)=", len(r))
html = etree.HTML(r, etree.HTMLParser())
r1 = html.xpath("//h3")
# print('r1=', r1)
# r2 = html.xpath('//*[@class="c-abstract"]')
r2 = html.xpath('//*[@class="content-right_8Zs40"]')
# print('r2=', r2)
# r3 = html.xpath('//*[@class="t"]/a/@href')
r3 = html.xpath("//a/@href")
print("r3=", r3)
for i in range(10):
    print("i=", i)
    if len(r1) > 0:
        if not (len(r1) > i and len(r2) > i and len(r3) > i):
            print("break")
            break
        r11 = r1[i].xpath("string(.)")
        r22 = r2[i].xpath("string(.)")
        r33 = r3[i]
        with open(data_folder + "/party_history.txt", "a", encoding="utf-8") as c:
            c.write(json.dumps(r11, ensure_ascii=False) + "\n")
            c.write(json.dumps(r22, ensure_ascii=False) + "\n")
            c.write(json.dumps(r33, ensure_ascii=False) + "\n")
            c.write("------------------------\n")
        print(r11, end="\n")
        print("------------------------")
        print(r22, end="\n")
        print(r33)
