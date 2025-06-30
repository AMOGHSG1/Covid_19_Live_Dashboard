COVID-19 Live Dashboard

Overview
This project delivers a real-time COVID-19 dashboard powered by a complete data pipeline. The system fetches global COVID-19 statistics hourly using the Disease.sh API, stores the data in a PostgreSQL database, and visualizes it using Microsoft Power BI.

Architecture Diagram

   ![image](https://github.com/user-attachments/assets/0daffa33-fe2b-4e90-bc76-a78ac09bb639)


---

## ⚙️ Technology Stack

| Component       | Tool               |
|----------------|--------------------|
| Data Source     | Disease.sh API     |
| Backend Script  | Python             |
| Data Cleaning   | pandas             |
| Scheduler       | APScheduler        |
| Database        | PostgreSQL         |
| Visualization   | Power BI           |

---

## 📜 Python Script Details

**File:** `hourly_api.py`

This script:
- Fetches live COVID-19 data hourly from Disease.sh API
- Cleans and renames selected fields using `pandas`
- Adds audit timestamps (`last_updated`, `fetch_time`)
- Saves cleaned data to PostgreSQL table (`covid_stats`), replacing old data for freshness

### 📦 Python Libraries Used
- `requests` – API calls  
- `pandas` – Data manipulation  
- `datetime` – Timestamps  
- `sqlalchemy` – PostgreSQL integration  
- `apscheduler` – Hourly task automation  

---

## 🧱 Database Schema

**Table:** `covid_stats`

| Column             | Description                       |
|--------------------|-----------------------------------|
| `country`          | Country name                      |
| `cases`            | Total confirmed cases             |
| `today_cases`      | Cases reported today              |
| `deaths`           | Total deaths                      |
| `today_deaths`     | Deaths reported today             |
| `recovered`        | Total recovered patients          |
| `active`           | Currently active cases            |
| `critical`         | Critical condition cases          |
| `cases_per_million`| Cases per 1 million population    |
| `deaths_per_million`| Deaths per 1 million population  |
| `tests`            | Total tests conducted             |
| `tests_per_million`| Tests per 1 million population    |
| `population`       | Country population                |
| `continent`        | Continent                         |
| `last_updated`     | API's last updated time           |
| `fetch_time`       | Script fetch timestamp            |

---

## 📊 Power BI Dashboard

- Connects directly to the PostgreSQL `covid_stats` table
- Live-refresh enabled (hourly)
- Interactive filters and visuals

### Key Visuals:
- 🌍 Global and country-level trends
- 📈 Time series of new cases and deaths
- 🗺️ Map of cases by country
- 📊 Histogram of cases per million (risk distribution)
- 🌐 Continent-wise comparisons
- 🔎 Country & continent slicers

**File:** `Covid_live.pbip`

---

## 📸 Screenshots

> _![image](https://github.com/user-attachments/assets/4c442a6d-9940-4b4f-be5c-5c5f9330490e)
  
> _Or embed a Power BI report link if published_

---

## ✅ Conclusion

This real-time COVID-19 dashboard is fully automated and scalable. It can be extended for:
- Vaccination data
- Predictive time series modeling
- Health alerts or notifications
- Cross-dataset integration (e.g., mobility or weather data)

---

## 📌 Author

**Amogh Shrinivas Goudar**  
_Data Analyst | Python | SQL | Power BI_  
[LinkedIn](https://www.linkedin.com) | [Portfolio](https://yourportfolio.com) *(Add yours)*

---

## 📁 License

MIT License — feel free to use or extend!
