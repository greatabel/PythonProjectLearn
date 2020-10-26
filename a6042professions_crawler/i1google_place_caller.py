import googlemaps
from os import environ
import time

from  place import Place
from  csv_operation import csv_writer_places_to_local
from i2place_detail import _get_place_details

api_key = environ.get('GOOGLE_CLOUD_API_KEY', '')
gmaps = googlemaps.Client(key=api_key)


destination = 'LakeWorth'

mymakets_A = ['Barber', 'Beautician', 'Make up Artist',
 "Nail tech(Nail artist) Esthetician'", 'Massage therapist']

mymakets_B = ['Beautician', 'Make up Artist',
 "Nail tech(Nail artist)"]


def result_to_plcae_obj(result):
    opening_hours = None
    if 'opening_hours' in result:
        opening_hours = result['opening_hours']
    p = Place(
        result['business_status'], result['formatted_address'], 
        result['name'], opening_hours, 
        result['plus_code'], result['rating'], 
        result['types'], result['user_ratings_total'])
    return p


places = []
def printHotels(searchString, next=''):

    try:
        places_result = gmaps.places(query=searchString, page_token=next)
    except ApiError as e:
        print(e)
    else:
        for result in places_result['results']:
            print(result['name'], '#'*10, result['place_id'])         
            print(result)
            r = _get_place_details(result['place_id'], api_key)
            print('@'*10, r, '@'*10, '\n')
            p = result_to_plcae_obj(result)

            places.append(p)
    time.sleep(2)
    try:
        places_result['next_page_token']
        print('-'*20, places_result['next_page_token'])
    except KeyError as e:
        print('Complete')
    else:
        printHotels(searchString, next=places_result['next_page_token'])



if __name__ == "__main__":
    printHotels(mymakets_A[0] + ' near ' + destination)
    print(len(places), places[0])
    csv_writer_places_to_local(places, destination+'.csv')


