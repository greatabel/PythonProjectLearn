import googlemaps
from os import environ


api_key = environ.get('GOOGLE_CLOUD_API_KEY', '')
gmaps = googlemaps.Client(key=api_key)


destination = 'LakeWorth'

mymakets = ['Barber', 'Beautician', 'Make up Artist',
 'Nail tech(Nail artist) Esthetician', 'Massage therapists']
local = gmaps.places(mymakets[0] + ' near ' + destination)

t0 = local['results']
print(t0)