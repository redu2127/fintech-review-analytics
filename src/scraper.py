import pandas as pd
from google_play_scraper import reviews, Sort

APPS = {
    "CBE": "com.combanketh.mobilebanking",
    "BOA": "com.boa.boaMobileBanking",
    "Dashen": "com.dashen.dashensuperapp",
}

def scrape_reviews(app_id, bank, count=500):
    result, _ = reviews(
        app_id,
        lang="en",
        country="et",
        sort=Sort.NEWEST,
        count=count,
    )

    data = []
    for r in result:
        data.append({
            "review_id": r.get("reviewId"),
            "review": r.get("content"),
            "rating": r.get("score"),
            "date": r.get("at"),
            "bank": bank,
            "source": "Google Play"
        })

    return pd.DataFrame(data)


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

    cleaned.to_csv("data/processed/cleaned_reviews.csv", index=False)
    print("Saved to data/processed/cleaned_reviews.csv")


if __name__ == "__main__":
    main()