import yfinance as yf
import json
import numpy as np
import os

SYMBOLS = ['APPL','MSFT','AMZN','NVDA','GOOGL','TSLA','META','UNH','XOM','AVGO','JPM','LLY','V','JNJ','HD','MA','PG','COST','ABBV','MRK','ADBE','CVX','CRM']

#creating and updating data into a file 
for symbol in SYMBOLS:
    stock = yf.Ticker(symbol)
    data = stock.info
    file_name = f'C:/D/Other/Data Engineering/yfinance/stockout/{symbol}.json'

    if os.path.exists(file_name):
        # If the file exists, load the existing data
        with open(file_name, 'r') as file:
            existing_data = json.load(file)

        # Update existing data with new data
        existing_data.update(data)

        # Write the updated data back to the file
        with open(file_name, 'w') as file:
            json.dump(existing_data, file, indent=4)
        print(f'Updated {symbol} data and saved to {file_name}')
    else:
        # If the file doesn't exist, create a new JSON file with fetched data
        with open(file_name, 'w') as file:
            json.dump(data, file, indent=4)
        print(f'Created new file for {symbol} and saved to {file_name}')


