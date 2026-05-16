import pandas as pd
from src.scraper import clean_reviews


def test_clean_data_removes_duplicates_and_missing_reviews():
    df = pd.DataFrame({
        "review_id": ["1", "1", "2"],
        "review": ["Good app", "Good app", None],
        "rating": [5, 5, 3],
        "date": ["2026-05-01", "2026-05-01", "2026-05-02"],
        "bank": ["CBE", "CBE", "BOA"],
        "source": ["Google Play", "Google Play", "Google Play"]
    })

    cleaned = clean_reviews(df)

    assert len(cleaned) == 1
    assert list(cleaned.columns) == ["review", "rating", "date", "bank", "source"]