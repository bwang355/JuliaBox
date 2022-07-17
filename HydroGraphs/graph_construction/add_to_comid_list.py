import warnings

import time
import os
import pandas as pd
import numpy as np
import json
from shapely.ops import nearest_points
from shapely.geometry import MultiPoint
import matplotlib.dates as mdates
import math
pd.options.display.max_columns = 50
pd.options.display.max_rows=50
import matplotlib.pyplot as plt
import matplotlib.cm
import matplotlib.colors as colors
import rtree
import geopandas as gpd
import pandas as pd
from scipy.interpolate import interp1d
import datetime
import scipy.stats as st
from scipy.optimize import curve_fit
from tqdm import tqdm
from WI_graph_functions import *
warnings.filterwarnings('ignore')

# Read in the tofrom lists from the NHDPlusV2 data
tofroms4 = pd.read_csv("lakes_rivers/Watershed4/PlusFlow.csv")
tofroms7 = pd.read_csv("lakes_rivers/Watershed7/PlusFlow.csv")

# Concatenate the data from the 04 and 07 HUC2 watersheds
tofroms = pd.concat([tofroms4, tofroms7])

# Read in the Wisconsin lake and river dataframes
WILakes  = pd.read_pickle("WILakes.df")
WIRivers = pd.read_pickle("WIRivers.df")

# Remove all tofrom listings that include a node not in the Wisconsin geodataframes
WItofroms = tofroms[(tofroms.TOCOMID.isin(WIRivers.COMID.values)) & (tofroms.FROMCOMID.isin(WIRivers.COMID.values))].copy()
WItofroms = WItofroms.reset_index(drop=True)

# Save the new CSV list of tofroms
WItofroms.to_csv("WIgeodataframes/WItofroms.csv")

# Add the waterbodies to the tofrom list.
WItofroms_lakes = add_to_tofroms(WItofroms, WIRivers, WILakes)

# Save the new CSV list of tofroms that includes waterbodies
WItofroms_lakes.to_csv("WIgeodataframes/WItofroms_lakes.csv")