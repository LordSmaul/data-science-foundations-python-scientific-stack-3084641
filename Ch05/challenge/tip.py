"""
- Load the taxi data.
- Remove all rows with either total_amount <= 0 or
  passenger_count == 0
- Create a bar chart of average tip % per passenger_count
- Create a bar chart of average tip % per day of week
"""

# %%
import pandas as pd

times = ['tpep_pickup_datetime', 'tpep_dropoff_datetime']
vendors = {1: 'Creative', 2: 'VeriFone'}

data = pd.read_csv('taxi.csv', parse_dates=times)
data['Vendor'] = data['VendorID'].map(vendors).astype('category')

# %%
drops = data[(data['total_amount'] <= 0) | (data['passenger_count'] == 0)]
data.drop(drops.index, inplace=True)

data['tips'] = data['tip_amount'] / data['total_amount'] * 100

# %%

group = data.groupby('passenger_count')['tips'].mean()

ax = group.plot.bar(title='Tip % by Passenger Count', rot=0)
ax.set_ylabel('Tip %')

from calendar import day_abbr

week_day = data['tpep_pickup_datetime'].dt.weekday
day = data.groupby(week_day)['tips'].mean()

day.index.name = 'Day of Week'
ax = day.plot.bar(title='Tip % of Day', rot=45)
ax.set_ylabel('Tip %')
ax.set_xticklabels([day_abbr[v] for v in ax.get_xticks()])
