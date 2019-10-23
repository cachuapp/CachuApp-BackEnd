#pip install googlemaps
#pip install prettyprint
#ativar cobrança

import googlemaps
import pprint
import time
#from GoogleMapsAPIKey import get_my_key

#Define our API key
API_KEY = 'AIzaSyCgYcfsAK2BU2v3c9E4UHPLSTkRqRe-Lxg' #get_my_key()

#Define our client
gmaps = googlemaps.Client(key = API_KEY)

#Define our search
places_result = gmaps.places(query= 'cachoeira', language = 'pt-BR')

pprint.pprint(places_result)