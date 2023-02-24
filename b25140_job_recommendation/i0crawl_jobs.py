import time
import csv
import requests
from bs4 import BeautifulSoup

url = 'https://findajob.dwp.gov.uk/search?cat=28'
page_number = 1

with open('data/jobs.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Description'])

    while True:
        response = requests.get(f'{url}&page={page_number}')
        soup = BeautifulSoup(response.content, 'html.parser')

        job_listings = soup.find_all('div', class_='search-result')

        if len(job_listings) == 0:
            # No more job listings, break out of the loop
            break

        for job in job_listings:
            h3_content = job.find('h3').text.strip()
            title_words = h3_content.split()
            title = ' '.join(word for word in title_words if not word.isnumeric())
            description = job.find('p', class_='govuk-body search-result-description').text.strip()
            print(title, description)
            print('#'*20)
            writer.writerow([title, description])
            time.sleep(1)
        page_number += 1

