import pandas as pd
from google_play_scraper import reviews, Sort

APPS = {
    "CBE": "com.combanketh.mobilebanking",
    "BOA": "com.boa.boaMobileBanking",
    "Dashen": "com.dashen.dashensuperapp",
}

def scrape_reviews(app_id, bank_name, count=500):

    try:
        result, _ = reviews(
            app_id,
            lang="en",
            country="et",
            sort=Sort.NEWEST,
            count=count
        )

        reviews_data = []

        for r in result:
            reviews_data.append({
                "review_id": r.get("reviewId"),
                "review": r.get("content"),
                "rating": r.get("score"),
                "date": r.get("at"),
                "bank": bank_name,
                "source": "Google Play"
            })

        return pd.DataFrame(reviews_data)

    except Exception as e:
        print(f"Error scraping reviews for {bank_name}: {e}")
        return pd.DataFrame()


def clean_reviews(df):
    before = len(df)

    df = df.drop_duplicates(subset=["review_id"])
    df = df.dropna(subset=["review", "rating"])
    df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")

    final_df = df[["review", "rating", "date", "bank", "source"]]

    print(f"Before cleaning: {before}")
    print(f"After cleaning: {len(final_df)}")
    print(f"Removed rows: {before - len(final_df)}")

    return final_df


def main():
    all_reviews = []

    for bank, app_id in APPS.items():
        print(f"Scraping {bank}...")
        df = scrape_reviews(app_id, bank, count=500)
        all_reviews.append(df)

    combined = pd.concat(all_reviews, ignore_index=True)
    cleaned = clean_reviews(combined)
    cleaned_df = cleaned
    try:
        cleaned_df.to_csv(
        "data/processed/cleaned_reviews.csv",
        index=False
        )

        print("CSV saved successfully!")

    except Exception as e:
        print(f"Error saving cleaned dataset: {e}")


if __name__ == "__main__":
    main()