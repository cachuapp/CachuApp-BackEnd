#pip install googlemaps
#pip install prettyprint

import googlemaps
import pprint
import time
from GoogleMapsAPIKey import get_my_key

#get data from Google API
def getData(gmaps):
    #Define our search
    places_result = gmaps.places(query= 'cachoeira', language = 'pt-BR') #or type = 'natural_feature' or type = 'tourist_attraction'
    #print(places_result)
    pprint.pprint(places_result)
    return places_result
    
def getNextPage(gmaps, places_result):
    #pause the script for 3 seconds
    time.sleep(3)
    #get the next 20 results
    places_result = gmaps.places(query= 'cachoeira', language = 'pt-BR', page_token = places_result['next_page_token'])
    pprint.pprint(places_result)
    return places_result
    
if __name__ == '__main__':
  #Define our API key
  API_KEY = get_my_key()
  
  #Define our client
  gmaps = googlemaps.Client(key = API_KEY)
  
  places_result = getData(gmaps)
  
  while('next_page_token' in places_result):
      new_places_result = getNextPage(gmaps, places_result)
      places_result = new_places_result