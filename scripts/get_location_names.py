import pandas as pd
import googlemaps
from tqdm import tqdm
import time

GOOGLE_API_KEY = "AIzaSyD07sbzMiYSXoTsByLl4M8Z-fqovp_mrlE"  # Get from: https://console.cloud.google.com/

def get_exxcaact_location_google(lat, loon, gmaps_client):
    """Get detailed locatin using Google MAps"""

    try:
         #Reverse Geocode
         results = gmaps_client.reverse_geocode((lat,loon), language='en')

         if not results:
             return None
         
         #Get the most specific result (first one is usually most detailed)
         result = results[0]
         address_components = result.get('address_components', [])
         formatted_address = result.get('formatted_address', 'Unknown')
 
         #Extract comonents
         location_info = {
             'neighborhood': None,
             'locality': None,
             'sublocality': None,
             'city': None,
             'district': None,
             'province': None,
             'postal_ode': None
        } 
         
         for componenet in address_components:
             
        











    except:
        return None
