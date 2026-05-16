import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/processed/analyzed_reviews.csv")

sns.set_style("whitegrid")

# Sentiment distribution
plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="bank",
    hue="sentiment_label"
)

plt.title("Sentiment Distribution by Bank")
plt.xlabel("Bank")
plt.ylabel("Number of Reviews")

plt.tight_layout()

plt.savefig("data/processed/sentiment_distribution.png")

plt.show()


# Rating distribution
plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df,
    x="bank",
    y="rating"
)

plt.title("Rating Distribution by Bank")
plt.xlabel("Bank")
plt.ylabel("Rating")

plt.tight_layout()

plt.savefig("data/processed/rating_distribution.png")

plt.show()


# Theme frequency
plt.figure(figsize=(10, 6))

theme_counts = df["identified_theme"].value_counts()

sns.barplot(
    x=theme_counts.values,
    y=theme_counts.index
)

plt.title("Theme Frequency")
plt.xlabel("Count")
plt.ylabel("Theme")

plt.tight_layout()

plt.savefig("data/processed/theme_frequency.png")

plt.show()


print("Visualizations generated successfully!")