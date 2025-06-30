import requests
import pandas as pd
from datetime import datetime

# Step 1: Define the API URL
API_URL = "https://disease.sh/v3/covid-19/countries"

# Step 2: Fetch data from API
response = requests.get(API_URL)

# Step 3: Check if response is successful
if response.status_code == 200:
    data = response.json()
    print(f"✅ Data fetched successfully. Total countries: {len(data)}")
else:
    print(f"❌ Failed to fetch data. Status code: {response.status_code}")
    exit()

# Step 4: Normalize data to DataFrame
df = pd.json_normalize(data)

# Step 5: Select relevant columns
df = df[[
    'country',
    'cases',
    'todayCases',
    'deaths',
    'todayDeaths',
    'recovered',
    'active',
    'critical',
    'casesPerOneMillion',
    'deathsPerOneMillion',
    'tests',
    'testsPerOneMillion',
    'population',
    'continent',
    'updated'
]]

# Step 6: Convert timestamp
df['last_updated'] = pd.to_datetime(df['updated'], unit='ms')
df.drop(columns=['updated'], inplace=True)

# Step 7: Add fetch date
df['fetch_time'] = datetime.utcnow()

# Step 8: Save to CSV (optional)
df.to_csv('covid_country_data.csv', index=False)
print("📁 Data saved to 'covid_country_data.csv'")

# Preview
print(df.head())
