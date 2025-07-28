# Skill Program Impact Analyzer

**Analyzing the Reach and Effectiveness of Indian Government Skill Development Programs**

---

## Project Overview

This project evaluates the real-world impact of government skill development schemes (PMKVY, DDU-GKY, NSDC programs) on Indian youth and underprivileged populations.

🔍 Focus areas:
- Who is enrolling? (demographic reach)
- Who is benefiting? (employment outcomes)
- How effective are the training centers?
- Where do dropouts happen, and why?

---

## Tech Stack

| Layer          | Tools/Frameworks                                       |
|----------------|--------------------------------------------------------|
| Database       | PostgreSQL (relational schema design, foreign keys)    |
| ETL            | Python (Pandas + Psycopg2)                             |
| Visualization  | Streamlit, Plotly                                      |
| Data Handling  | CSV (for initial load), Pandas                         |
| Future Plans   | Scikit-learn (ML prediction), VADER/spaCy (NLP)        |

---

## Current Features

### 1. Relational Database with Normalized Schema
PostgreSQL schema includes:
- `beneficiaries`
- `programs`
- `training_centres`
- `locations`
- `employment_outcomes`
- `assessments`
- `feedback`

Foreign key constraints ensure data integrity.

---

### 2. CSV Data Generator & Loader
- Scripts create mock data (~30 records per table).
- Python ETL pipeline loads the data into PostgreSQL.

---

### 3. Interactive Streamlit Dashboard
- Gender-wise enrollment distribution
- Dropout vs. completion ratio
- Program-wise average salary outcomes
- Real-time data fetch using SQL joins from DB

---

## Folder Structure

skill\_impact\_analyzer/
│
├── data/                  # CSV data files (mock or scraped)
├── db/                    # SQL schema creation scripts
├── etl/                   # Python scripts to load data into PostgreSQL
├── app/                   # Streamlit dashboard code
├── utils/                 # Helper functions (planned)
├── outputs/               # Generated reports (planned)
├── README.md
└── requirements.txt

---

## Future Roadmap

### ML Module
> Predict likelihood of employment based on age, education, program type, etc.

- Logistic Regression / XGBoost
- Accuracy, F1-score tracking
- Integration with dashboard

### NLP on Feedback
> Analyze sentiment, detect skill mismatch patterns.

- Sentiment scoring (VADER)
- Keyword extraction
- LDA Topic Modeling

### Geospatial Analysis
> Plot state-wise disparities using Plotly/Folium.

---

## How to Use

1. **Setup PostgreSQL locally**
2. `python generate_csvs.py` – creates mock data
3. `python etl/load_to_postgres.py` – loads into DB
4. `streamlit run app/dashboard.py` – launches interactive dashboard


