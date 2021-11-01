from __init__ import get_id
import googlemaps
import json
from datetime import datetime

def generate(api_key, query, location, name):
    gmaps = googlemaps.Client(key=api_key)
    # Geocoding an address
    place_id_restaurant = gmaps.places(type=query, location = location)
    places = []

    for restaurant in place_id_restaurant['results']:
        places.append(restaurant['place_id'])

    popular_times = []

    for place_id in places:
        popular_times.append(get_id(api_key,place_id))

    with open(name+'.json', 'w') as file:
        json.dump(popular_times, file, indent=4)


api_key = ""

Zona_T = {
        "lat" : 4.6676124,
        "lng" : -74.0541186
    }

Zona_G = {
    "lat" : 4.6527407,
    "lng" : -74.0553762
}

Usaquen = {
    "lat" : 4.6767219,
    "lng" : -74.0482788
}

Chapinero = {
    "lat" : 4.6486981,
    "lng" : -74.030198
}

zonas = [[Zona_T, "Zona_T"], [Zona_G, "Zona_G"], [Usaquen, "Usaquen"], [Chapinero, "Chapinero"]]

#Tipos de busqueda: https://developers.google.com/maps/documentation/places/web-service/supported_types
#restaurant - gym - casino - cafe - bank - bar
query = "restaurant"

for z in range(len(zonas)):
    generate(api_key, query, zonas[z][0], zonas[z][1]+"_"+str(datetime.now().date()))

