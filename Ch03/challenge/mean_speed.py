# What is the mean speed (mile/hour) in taxi.parquet?

# - Run download_data.py to download the data
# %%
import pandas as pd

data = pd.read_parquet('taxi.parquet')
data.head()

# %%
data.info()

# %%
data = data[data['tpep_dropoff_datetime'] > data['tpep_pickup_datetime']]

# %%
times = data['tpep_dropoff_datetime'] - data['tpep_pickup_datetime']
hours = times / pd.Timedelta(1, 'hour')

speed = data['trip_distance'] / hours

# %%
print(speed.mean())
