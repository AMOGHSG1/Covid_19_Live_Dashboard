from apscheduler.schedulers.blocking import BlockingScheduler
import pandas as pd
import requests
from datetime import datetime
from sqlalchemy import create_engine

# 🔧 PostgreSQL credentials
DB_USER = 'add user '         # <-- change this
DB_PASS = 'add password'         # <-- change this
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'Covid_Live'
TABLE_NAME = 'covid_stats'

# ✅ Use correct SQLAlchemy format (with +psycopg2)
DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

# ⏰ Scheduler setup
scheduler = BlockingScheduler()

def fetch_and_store():
    print(f"\n⏰ Fetching at {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC")
    url = "https://disease.sh/v3/covid-19/countries"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        df = pd.json_normalize(data)

        # 🎯 Select only relevant columns
        df = df[[
            'country', 'cases', 'todayCases', 'deaths', 'todayDeaths',
            'recovered', 'active', 'critical', 'casesPerOneMillion',
            'deathsPerOneMillion', 'tests', 'testsPerOneMillion',
            'population', 'continent', 'updated'
        ]]

        # 🧹 Rename columns and add timestamps
        df['last_updated'] = pd.to_datetime(df['updated'], unit='ms')
        df['fetch_time'] = datetime.utcnow()
        df.drop(columns=['updated'], inplace=True)

        df.columns = [
            'country', 'cases', 'today_cases', 'deaths', 'today_deaths',
            'recovered', 'active', 'critical', 'cases_per_million',
            'deaths_per_million', 'tests', 'tests_per_million',
            'population', 'continent', 'last_updated', 'fetch_time'
        ]

        # 💾 Store in PostgreSQL (overwrite table)
        df.to_sql(TABLE_NAME, con=engine, if_exists='replace', index=False)
        print("✅ Data written to PostgreSQL")

    except Exception as e:
        print("❌ Error:", e)

# 🔁 Schedule job every hour
scheduler.add_job(fetch_and_store, 'interval', hours=1)
fetch_and_store()  # Run once immediately
scheduler.start()
