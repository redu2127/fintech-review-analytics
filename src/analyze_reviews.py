import pandas as pd
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer


def get_sentiment(text):
    polarity = TextBlob(str(text)).sentiment.polarity

    if polarity > 0.1:
        label = "positive"
    elif polarity < -0.1:
        label = "negative"
    else:
        label = "neutral"

    return label, polarity


def assign_theme(review):
    text = str(review).lower()

    if any(word in text for word in ["login", "password", "otp", "pin", "access"]):
        return "Account Access Issues"
    elif any(word in text for word in ["transfer", "transaction", "send", "payment"]):
        return "Transaction Performance"
    elif any(word in text for word in ["crash", "slow", "loading", "error", "bug"]):
        return "App Reliability and Performance"
    elif any(word in text for word in ["interface", "ui", "easy", "design", "user friendly"]):
        return "User Interface and Experience"
    elif any(word in text for word in ["feature", "fingerprint", "update", "budget"]):
        return "Feature Requests"
    else:
        return "General Feedback"


def extract_keywords(df):
    vectorizer = TfidfVectorizer(
        stop_words="english",
        max_features=20,
        ngram_range=(1, 2)
    )

    tfidf_matrix = vectorizer.fit_transform(df["review"].astype(str))
    keywords = vectorizer.get_feature_names_out()

    return keywords


def main():
    df = pd.read_csv("data/processed/cleaned_reviews.csv")

    df["review_id"] = range(1, len(df) + 1)

    sentiment_results = df["review"].apply(get_sentiment)
    df["sentiment_label"] = sentiment_results.apply(lambda x: x[0])
    df["sentiment_score"] = sentiment_results.apply(lambda x: x[1])

    df["identified_theme"] = df["review"].apply(assign_theme)

    output_df = df[
        [
            "review_id",
            "review",
            "sentiment_label",
            "sentiment_score",
            "identified_theme",
            "rating",
            "date",
            "bank",
            "source"
        ]
    ]

    output_df = output_df.rename(columns={"review": "review_text"})

    output_df.to_csv("data/processed/analyzed_reviews.csv", index=False)

    print("Sentiment and theme analysis completed.")
    print(output_df["sentiment_label"].value_counts())
    print(output_df["identified_theme"].value_counts())

    for bank in df["bank"].unique():
        print(f"\nTop keywords for {bank}:")
        bank_df = df[df["bank"] == bank]
        print(extract_keywords(bank_df))


if __name__ == "__main__":
    main()