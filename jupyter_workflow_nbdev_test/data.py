# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/dr00.ipynb.

# %% auto 0
__all__ = ['FREMONT_URL', 'get_fremont_data']

# %% ../nbs/dr00.ipynb 4
from pathlib import Path
from urllib.request import urlretrieve

import pandas as pd

# %% ../nbs/dr00.ipynb 5
FREMONT_URL= "https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD"

# %% ../nbs/dr00.ipynb 6
def get_fremont_data(filename:str="Fremont.csv", # Location to save the data
                     url:str=FREMONT_URL, # Web location for the data
                     force_download:bool=False # if True, force redownload the data
                    ) -> pd.DataFrame: # The Fremont bridge data
    if force_download or not Path(filename).exists():
        urlretrieve(url, filenmae)
    data = pd.read_csv(filename, index_col="Date")
    try:
        data.index = pd.to_datetime(data.index, format="%m/%d/%Y %I:%M:%S %p")
    except TypeError:
        data.index = pd.to_datetime(data.index)
    data.columns = ["Total", "East", "West"]
    return data
