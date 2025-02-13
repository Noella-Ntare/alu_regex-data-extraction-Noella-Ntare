import re

def extract_emails(text):
    """Extracts all valid email addresses from the text."""
    email_pattern = r"[\w\.-]+@[\w\.-]+\.\w{2,}"
    matches = re.findall(email_pattern, text)
    return matches if matches else ["No valid emails found"]

def extract_urls(text):
    """Extracts all valid URLs from the text."""
    url_pattern = r"https?:\/\/[\w\-\.]+(\.[a-z]{2,})(\/\S*)?"
    matches = re.findall(url_pattern, text)
    return [match[0] for match in matches] if matches else ["No valid URLs found"]

def extract_phone_numbers(text):
    """Extracts phone numbers in various formats."""
    phone_pattern = r"(\(\d{3}\)\s?|\d{3}[-.])?\d{3}[-.]\d{4}"
    matches = re.findall(phone_pattern, text)
    return matches if matches else ["No valid phone numbers found"]

def extract_hashtags(text):
    """Extracts all valid hashtags from the text."""
    hashtag_pattern = r"#[A-Za-z0-9_]+"
    matches = re.findall(hashtag_pattern, text)
    return matches if matches else ["No valid hashtags found"]

