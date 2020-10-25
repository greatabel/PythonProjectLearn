import googlemaps
from os import environ
import time

api_key = environ.get('GOOGLE_CLOUD_API_KEY', '')
gmaps = googlemaps.Client(key=api_key)


destination = 'LakeWorth'

mymakets_A = ['Barber', 'Beautician', 'Make up Artist',
 "Nail tech(Nail artist) Esthetician'", 'Massage therapist']

mymakets_B = ['Beautician', 'Make up Artist',
 "Nail tech(Nail artist)"]


# def get_places():
#     local = gmaps.places(mymakets[0] + ' near ' + destination)
#     # https://developers.google.com/places/supported_types
#     #gmaps.places(location=(lat,lng), type="movie_theater")
#     # print(local)
#     print('\n'*3)
#     t0 = local['results']
#     print(t0)


def printHotels(searchString, next=''):
    try:
        places_result = gmaps.places(query=searchString, page_token=next)
    except ApiError as e:
        print(e)
    else:
        for result in places_result['results']:
            print(result['name'], '#'*10)
            print(result)
    time.sleep(2)
    try:
        places_result['next_page_token']
        print('-'*10, places_result['next_page_token'])
    except KeyError as e:
        print('Complete')
    else:
        printHotels(searchString, next=places_result['next_page_token'])



if __name__ == "__main__":
    printHotels(mymakets_A[0] + ' near ' + destination)