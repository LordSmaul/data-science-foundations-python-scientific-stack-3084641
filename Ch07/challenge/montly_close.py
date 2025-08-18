"""
Using the stock data from stocks.csv, draw a bar chart were:
- The x axis is the month
- The y axis is the median closing price
- Each stock should have it's own chart
"""
# %%
import pandas as pd

data = pd.read_csv('stocks.csv', parse_dates=['Date'])

data.head()

# %%

data['Month'] = data['Date'].dt.month
month_data = data.pivot_table(columns='Symbol', index='Month', values='Close', aggfunc='median')

month_data

# %%
from calendar import month_abbr

ax = month_data.plot.bar(title='Median Monthly Close', rot=0)
ax.set_xticklabels([month_abbr[i+1] for i in ax.get_xticks()])
ax.set_ylabel('Closing Price')
