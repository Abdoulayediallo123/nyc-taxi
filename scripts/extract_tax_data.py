import requests
import pandas as pd

url = "https://data.cityofnewyork.us/resource/gkne-dk5s.json?$limit=50000"
response = requests.get(url)
data = pd.DataFrame(response.json())

data.to_csv("/Users/abdoulayediallo/Documents/nyc_taxi/raw_taxi_data.csv", index=False)
print("Data extracted successfully.")
