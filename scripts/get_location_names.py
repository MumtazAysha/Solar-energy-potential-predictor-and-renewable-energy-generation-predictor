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
         
         for component in address_components:
             types = component.get('types', [])
             name = component.get('long_name', '')

             if 'neighborhood' in types:
                 location_info['neighborhod'] = name
             elif 'sublocality' in types or 'sublocality_level_1' in types:
                 location_info['sublocality'] = name
             elif 'locality' in types:
                 location_info['locality'] = name
             elif 'administrative_area_level_2' in types:
                 location_info['district'] = name
             elif 'administrative_area_level_1' in types:
                 location_info['province'] = name   
             elif 'postal_code' in types:
                 location_info['postal_code'] = name

        

             
        











    except:
        return None
