# Fintech Review Analytics

Customer Experience Analytics for Ethiopian mobile banking apps.

## Project Overview

This project analyzes Google Play Store reviews for three Ethiopian banks:

- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

The goal is to understand customer sentiment, identify recurring complaints and satisfaction drivers, and provide product recommendations for mobile banking improvement.

## Tasks Completed

### Task 1: Data Collection and Preprocessing
- Scraped Google Play Store reviews using `google-play-scraper`.
- Collected review text, rating, date, bank name, and source.
- Removed duplicates and missing values.
- Normalized dates to `YYYY-MM-DD`.
- Saved cleaned data as CSV locally.

### Task 2: Sentiment and Thematic Analysis
- Applied sentiment analysis to classify reviews as positive, negative, or neutral.
- Assigned sentiment scores.
- Grouped reviews into themes such as:
  - Account Access Issues
  - Transaction Performance
  - App Reliability and Performance
  - User Interface and Experience
  - Feature Requests

## Task 2: Sentiment and Thematic Analysis Output

The Task 2 pipeline is implemented in:

`src/analyze_reviews.py`

It reads the cleaned dataset from:

`data/processed/cleaned_reviews.csv`

and generates an analyzed dataset locally at:

`data/processed/analyzed_reviews.csv`

The analyzed dataset includes:

- review_id
- review_text
- sentiment_label
- sentiment_score
- identified_theme
- rating
- date
- bank
- source

The pipeline was designed to process the full cleaned review dataset, targeting at least 400 reviews per bank and at least 1,200 reviews overall.

Data files are excluded from GitHub using `.gitignore`, so the generated CSV is documented but not committed.

### Task 3: PostgreSQL Database
- Created PostgreSQL database named `bank_reviews`.
- Designed two tables:
  - `banks`
  - `reviews`
- Loaded processed review data into PostgreSQL using SQLAlchemy.

### Task 4: Insights and Recommendations
- Created visualizations for sentiment, ratings, and themes.
- Produced bank-specific insights and recommendations.
- Prepared a final insight report.

## Review Collection Summary

Reviews were collected from the Google Play Store for three Ethiopian banking applications: CBE, BOA, and Dashen Bank.

Target collection size:
- CBE: 400+ reviews
- BOA: 400+ reviews
- Dashen Bank: 400+ reviews
- Total target: 1,200+ reviews

The scraping was performed in May 2026 using the `google-play-scraper` package. Reviews were collected using the newest available reviews returned by the scraper.

Scraping constraints:
- Google Play review availability may vary by app.
- The exact date range depends on the reviews returned by Google Play at scraping time.
- If fewer reviews are returned for an app, the scraper can be rerun with a larger count parameter.
- Raw CSV files are excluded from GitHub using `.gitignore` to avoid committing data files.

## Project Structure

```text
fintech-review-analytics/
├── .github/workflows/unittests.yml
├── data/
├── notebooks/
├── reports/final_insights.md
├── scripts/schema.sql
├── src/
│   ├── scraper.py
│   ├── analyze_reviews.py
│   ├── load_to_postgres.py
│   └── visualize_insights.py
├── tests/test_preprocessing.py
├── README.md
├── requirements.txt
├── pytest.ini
└── .gitignore

## How to Run
### Install dependencies:
- pip install -r requirements.txt
###Run data scraping:
- python src/scraper.py
### Run sentiment and theme analysis:
- python src/analyze_reviews.py
###Load data into PostgreSQL:
- python src/load_to_postgres.py
### Generate visualizations:
- python src/visualize_insights.py
### Run tests:
- pytest

## Database Schema
The database contains two tables:
### banks
- bank_id
- bank_name
- app_name
### reviews
- review_id
- bank_id
- review_text
- rating
- review_date
- sentiment_label
- sentiment_score
- identified_theme
- source

## Tools Used
- Python
- pandas
- google-play-scraper
- TextBlob
- scikit-learn
- PostgreSQL
- SQLAlchemy
- Matplotlib
- Seaborn
- pytest
- GitHub Actions

##Limitations
- Google Play reviews may not represent all users.
- Some reviews are short or ambiguous.
- Sentiment analysis may misinterpret sarcasm or mixed emotions.
- Scraping results may vary depending on app availability and - - Google Play limitations.