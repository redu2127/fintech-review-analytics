from src.analyze_reviews import get_sentiment, assign_theme


def test_positive_sentiment_label():
    label, score = get_sentiment("This app is very good and easy to use")
    assert label == "positive"
    assert score > 0.1


def test_negative_sentiment_label():
    label, score = get_sentiment("This app is bad and very slow")
    assert label == "negative"
    assert score < -0.1


def test_neutral_sentiment_label():
    label, score = get_sentiment("Mobile banking application")
    assert label == "neutral"


def test_assign_login_theme():
    theme = assign_theme("OTP not received and login failed")
    assert theme == "Account Access Issues"


def test_assign_transaction_theme():
    theme = assign_theme("Transfer and transaction failed")
    assert theme == "Transaction Performance"