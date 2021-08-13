import os
import pickle
import pprint
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import csv

def csv_writer_places_to_local(places, filename):
    with open(filename, 'a') as csvfile:
        fieldnames = [ 'cityid', 'cityname', 'jobname',
                      'business_status', 'formatted_address', 'name',
                      'opening_hours', 'plus_code', 'rating', 'types',
                      'user_ratings_total']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for p in places:
            writer.writerow({
                'cityid': p.cityid,
                'cityname': p.cityname,
                'jobname': p.jobname,
                'business_status': p.business_status,
                'formatted_address': p.formatted_address,
                'name': p.name,
                'opening_hours': p.opening_hours,
                'plus_code': p.plus_code,
                'types': p.types,
                'rating': p.rating,
                'user_ratings_total': p.user_ratings_total
                            })


def csv_reader(filename, directory='./'):
    with open(os.path.join(directory, filename), newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        mylist = []
        for row in reader:
            mylist.append(row[0].split(','))    
        return mylist