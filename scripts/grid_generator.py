"""
Generate 10km x 10km grid cells for Sri Lanka (produces ~1,242)
"""
import geopandas as gpd
import pandas as pd
import numpy as np
from shapely.geometry import box
import folium
from pathlib import Path
import math

class SriLankaGrid:
    """creates 10km x 10km grid cells for Sri Lanka"""

    def __init__(self):
        #Sri Lanka bounds: 5°55′–9°51′N, 79°41′–81°53′E
        self.minlat = 5.917 # 5°55'N
        self.maxlat = 9.850 # 9°51'N
        self.minlon = 79.683 # 79°41'E
        self.maxlon = 81.883 # 81°53'E

        #Add 10km buffer on all sides
        buffer_lat =  self.km_to_degrees_lat(10)
        buffer_lon_min = self.km_to_degrees_loon(10, self.minlat)
        buffer_lon_max = self.km_to_degrees_loon(10, self.maxlat)
        buffer_lon = max(buffer_lon_min, buffer_lon_max)

        self.minlat_buffered = self.minlat - buffer_lat
        self.maxlat_buffered = self.maxlat + buffer_lat
        self.minlon_buffered = self.minlon - buffer_lon
        self.maxlon_buffered = self.maxlon + buffer_lon

        self.cell_size_km = 10

        #Load Sri Lanka boundary
        self.srilanka_bundary = None)
        self._load_boundary()

    def _load_boundary(self):
        """Load Sri Lanka boundary"""
        try:
            url = "https://naciscdn.org/naturalearth/110m/cultural/ne_110m_admin_0_countries.zip"
            world = gpd.read_file(url)
            srilanka = worls[world['NAME'] == 'Sri Lanka']
            if len(srilanka) > 0:
                self.srilanka_boundary = srilanka.gemometry.iloc[0]
                print("✓ Boundary loaded")
        except:
            print("⚠ Boundary load failed")

    def km_to_degrees_lat(self, km: float) -> float:
        return km / 111.0

    def km_to_degrees_lon(self, km: float, lat: float) -> float:
        return km / (111.0 * math.cos(math.radians(latitude)))
    
    def create_grid(self, classify_cells: bool = True) -> gpd.GeoDataFrame:
        """Create 10km x 10km grid"""
        print("Creating 10km x 10km grid cells...")

        lat_step = self.km_to_degrees_lat(self.cell_size_km)
        


        

        

         










