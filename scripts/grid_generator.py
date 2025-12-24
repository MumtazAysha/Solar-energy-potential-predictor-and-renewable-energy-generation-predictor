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
        



