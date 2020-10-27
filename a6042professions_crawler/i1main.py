import googlemaps
from os import environ
import time
import csv

from  place import Place
from  csv_operation import csv_writer_places_to_local, csv_reader
from i2place_detail import _get_place_details

api_key = environ.get('GOOGLE_CLOUD_API_KEY', '')
gmaps = googlemaps.Client(key=api_key)




mymakets_A = ['Barber', 'Beautician', 'Make up Artist',
 "Nail tech(Nail artist) Esthetician'", 'Massage therapist']

mymakets_B = ['Beautician', 'Make up Artist',
 "Nail tech(Nail artist)"]


def result_to_plcae_obj(cityid, cityname, jobname, result):
    opening_hours = None
    if 'opening_hours' in result:
        opening_hours = result['opening_hours']
    p = Place(
        cityid,
        cityname,
        jobname,
        result['business_status'], result['formatted_address'], 
        result['name'], opening_hours, 
        result['plus_code'], result['rating'], 
        result['types'], result['user_ratings_total'])
    return p



def printHotels(searchString='',cityid='', cityname='', jobname='', next=''):

    try:
        places_result = gmaps.places(query=searchString, page_token=next)
    except ApiError as e:
        print(e)
    else:
        for result in places_result['results']:
            print(result['name'], '#'*10, result['place_id'])         
            print(result)
            # 暂时不需要详细部分
            # r = _get_place_details(result['place_id'], api_key)
            # print('@'*10, r, '@'*10, '\n')
            p = result_to_plcae_obj(cityid, cityname, jobname, result)

            places.append(p)
    time.sleep(2)
    try:
        places_result['next_page_token']
        print('-'*20, places_result['next_page_token'])
    except KeyError as e:
        print('Complete')
    else:
        printHotels(searchString, cityid, cityname, jobname, next=places_result['next_page_token'])



if __name__ == "__main__":
    citylist = csv_reader('rank_cities.csv')
    print(citylist[0],citylist[0][0], citylist[0][1])
    destination = citylist[0][1]
    places = []
    printHotels(mymakets_A[0] + ' near ' + citylist[0][1],  citylist[0][0], citylist[0][1], mymakets_A[0])
    print(len(places), places[0], '#'*20)
    print('\n')
    printHotels(mymakets_A[0] + ' near ' +  citylist[1][1], citylist[1][0],citylist[1][1], mymakets_A[0])
    print(len(places), places[0], '#'*20)

    csv_writer_places_to_local(places, 
        'results/' + citylist[0][0] + '_' + destination+'.csv')


