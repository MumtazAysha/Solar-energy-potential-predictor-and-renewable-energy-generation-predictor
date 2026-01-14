import googlemaps

# Your API key
gmaps = googlemaps.Client(key="AIzaSyD07sbzMiYSXoTsByLl4M8Z-fqovp_mrlE")

# Test Colombo coordinates
result = gmaps.reverse_geocode((6.9271, 79.8612), language='en')
print("Colombo test:")
print(result[0]['formatted_address'] if result else "FAILED!")

# Test grid cell (use one from your CSV)
result2 = gmaps.reverse_geocode((7.29, 80.63), language='en')  # Kandy area
print("\nGrid cell test:")
print(result2[0]['formatted_address'] if result2 else "FAILED!")
