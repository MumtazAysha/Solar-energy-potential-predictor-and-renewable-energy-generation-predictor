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
         
         
    









    except:
        return None
