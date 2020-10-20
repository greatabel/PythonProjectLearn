from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import csv

rank_cities_csv = 'rank_cities.csv'

rank_cities = []
url = 'https://www.florida-demographics.com/cities_by_population'
response = urlopen(url)
html = response.read()

soup = BeautifulSoup(html, features="lxml")
tables = soup.findAll("table")
if len(tables) >= 1:
    table = tables[0]
    rows = table.findAll("tr")
    for row in rows:
        tds = row.findAll('td')
        if(len(tds) == 3):
            td0 = tds[0]
            

            rank = int(re.search(r'\d+', td0.contents[0]).group())
            # print(rank, '#'*10)
            if rank >= 100 and rank < 300:
                if rank == 100:
                    
                    # print(tds[1].contents[1], '#'*20, type(tds[1].contents[1]))
                    td1 = re.findall(r'>.+?</a>',str(tds[1].contents[1]))
                    td1 = td1[0].replace('</a>', '').replace('>', '')
                    # print(td1)
                else:
                    td1 = tds[1].contents[0]
                city   = re.sub(r"[\n\t\s]*", "", td1)
                rank_cities.append([rank, city])
                print(rank, city)




with open(rank_cities_csv, mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in rank_cities:
        employee_writer.writerow(row)

print('saved successed to', rank_cities_csv)