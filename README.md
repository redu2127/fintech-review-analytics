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