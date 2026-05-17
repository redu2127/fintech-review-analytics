# Customer Experience Analytics for Ethiopian Fintech Apps

## Executive Summary

This project analyzed Google Play Store reviews from:
- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

The analysis included:
- Review scraping
- Data preprocessing
- Sentiment analysis
- Thematic analysis
- PostgreSQL database integration
- Data visualization

---

# Commercial Bank of Ethiopia (CBE)

## Satisfaction Drivers
- Users appreciated fast transaction processing.
- Many reviews praised the app interface and ease of use.

## Pain Points
- Login and OTP verification issues appeared frequently.
- Some users reported crashes during transfers.

## Recommendations
- Improve OTP reliability and authentication stability.
- Optimize app performance during peak transaction periods.

---

# Bank of Abyssinia (BOA)

## Satisfaction Drivers
- Positive feedback on mobile transfer features.
- Users liked the app accessibility.

## Pain Points
- High number of complaints regarding app slowness.
- Frequent account access and password reset problems.

## Recommendations
- Improve backend performance and server response time.
- Simplify account recovery workflows.

---

# Dashen Bank

## Satisfaction Drivers
- Users appreciated the modern UI design.
- Reviews indicated relatively stable transaction performance.

## Pain Points
- Some complaints about update-related bugs.
- Feature request frequency was high.

## Recommendations
- Improve testing before app updates.
- Prioritize requested features like biometric login.

---

# Comparative Insights

- CBE and Dashen showed more positive sentiment overall.
- BOA received more complaints related to performance and access issues.
- Transaction reliability and authentication remain critical user concerns across all banks.

---

## Sentiment and Thematic Analysis Scale

The sentiment and thematic analysis pipeline was applied to the cleaned review dataset generated from Task 1. The project targeted at least 400 reviews per bank, giving a minimum target of 1,200 reviews across CBE, BOA, and Dashen Bank.

Each review was processed to generate:
- sentiment_label
- sentiment_score
- identified_theme

The final analyzed output was saved locally as:

`data/processed/analyzed_reviews.csv`

This file was not committed to GitHub because data files are excluded through `.gitignore`.

# Ethical Considerations

- Only publicly available review data was used.
- No personal or sensitive customer information was collected.

---

# Limitations

- Google Play reviews may not represent all users.
- Some reviews were short or ambiguous.
- Sentiment classification may misinterpret sarcasm or mixed emotions.

---

# Suggested Next Steps

- Deploy real-time sentiment monitoring dashboards.
- Integrate AI-powered customer support chatbots.
- Use transformer-based models for improved sentiment accuracy.