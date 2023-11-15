# Import Pandas
import pandas as pd

# Show all data
pd.read_csv('dataset\\2016-12-31-to-2023-11-06-btc-usd.csv')

price_close = pd.read_csv('dataset\\2016-12-31-to-2023-11-06-btc-usd.csv', index_col='Date', parse_dates=['Date'], usecols=['Date','Close'])
print('Price - Close:\n',price_close)