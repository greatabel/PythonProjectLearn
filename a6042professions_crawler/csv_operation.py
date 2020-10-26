import os
import pickle
import pprint
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import csv

def csv_writer_places_to_local(places, filename):
    with open(filename, 'a') as csvfile:
        fieldnames = ['business_status', 'formatted_address', 'name',
                      'opening_hours', 'plus_code', 'rating', 'types',
                      'user_ratings_total']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for p in places:
            writer.writerow({
                'business_status': p.business_status,
                'formatted_address': p.formatted_address,
                'name': p.name,
                'opening_hours': p.opening_hours,
                'plus_code': p.plus_code,
                'rating': p.rating,
                'types': p.types,
                'user_ratings_total': p.user_ratings_total
                            })