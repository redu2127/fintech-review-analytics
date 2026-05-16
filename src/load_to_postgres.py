import pandas as pd
from sqlalchemy import create_engine, URL

DB_USER = "postgres"
DB_PASSWORD = "@Rg65438634"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "bank_reviews"

url = URL.create(
    drivername="postgresql+psycopg2",
    username=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT,
    database=DB_NAME,
)

engine = create_engine(url)
df = pd.read_csv("data/processed/analyzed_reviews.csv")

banks_df = pd.DataFrame({
    "bank_name": ["CBE", "BOA", "Dashen"],
    "app_name": [
        "Commercial Bank of Ethiopia",
        "Bank of Abyssinia",
        "Dashen Bank"
    ]
})

banks_df.to_sql(
    "banks",
    engine,
    if_exists="append",
    index=False
)

bank_mapping = {
    "CBE": 1,
    "BOA": 2,
    "Dashen": 3
}

df["bank_id"] = df["bank"].map(bank_mapping)

reviews_df = df[
    [
        "bank_id",
        "review_text",
        "rating",
        "date",
        "sentiment_label",
        "sentiment_score",
        "identified_theme",
        "source"
    ]
]

reviews_df = reviews_df.rename(
    columns={"date": "review_date"}
)

reviews_df.to_sql(
    "reviews",
    engine,
    if_exists="append",
    index=False
)

print("Data inserted successfully!")