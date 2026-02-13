import re
from textblob import TextBlob


# Optional spell correction
def preprocess(text):
    return str(TextBlob(text).correct())


def calculate_score(text, keyword_dict):
    score = 0
    for word, weight in keyword_dict.items():
        if word in text:
            score += weight
    return score


def contains_url(text):
    pattern = r'https?://\S+|www\.\S+'
    return re.search(pattern, text)


def classify_issue(user_input):

    # Preprocess (spell correction)
    text = preprocess(user_input.lower())

    ransomware_keywords = {
        "encrypted": 3,
        "ransom": 3,
        "bitcoin": 2,
        "decrypt": 2,
        "locked files": 3
    }

    phishing_keywords = {
        "otp": 3,
        "bank": 2,
        "verify": 2,
        "urgent": 1,
        "login": 2,
        "account suspended": 3
    }

    malware_keywords = {
        "slow": 1,
        "popup": 2,
        "ads": 2,
        "virus": 3,
        "malware": 3
    }

    breach_keywords = {
        "password changed": 3,
        "hacked": 3,
        "account stolen": 3,
        "unauthorized login": 2
    }

    scores = {
        "ransomware": calculate_score(text, ransomware_keywords),
        "phishing": calculate_score(text, phishing_keywords),
        "malware": calculate_score(text, malware_keywords),
        "account_breach": calculate_score(text, breach_keywords)
    }

    # Extra boost if URL detected → phishing likely
    if contains_url(text):
        scores["phishing"] += 2

    threat = max(scores, key=scores.get)
    total_score = sum(scores.values())

    if total_score == 0:
        return "uncertain", 0

    confidence = scores[threat] / total_score

    # Confidence threshold
    if confidence < 0.4:
        return "uncertain", round(confidence, 2)

    return threat, round(confidence, 2)
