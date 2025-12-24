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

