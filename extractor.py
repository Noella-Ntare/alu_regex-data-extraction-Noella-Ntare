import re

def extract_emails(text):
    """Extracts all valid email addresses from the text."""
    email_pattern = r"[\w\.-]+@[\w\.-]+\.\w{2,}"
    return re.findall(email_pattern, text)

def extract_urls(text):
    """Extracts all valid URLs from the text."""
    url_pattern = r"https?:\/\/[\w\-\.]+(\.[a-z]{2,})(\/\S*)?"
    return re.findall(url_pattern, text)

def extract_phone_numbers(text):
    """Extracts phone numbers in various formats."""
    phone_pattern = r"(\(\d{3}\)\s?|\d{3}[-.])?\d{3}[-.]\d{4}"
    return re.findall(phone_pattern, text)

def extract_hashtags(text):
    """Extracts all valid hashtags from the text."""
    hashtag_pattern = r"#[A-Za-z0-9_]+"
    return re.findall(hashtag_pattern, text)

# Sample input (simulating API response)
sample_text = """
Contact us at user@example.com or firstname.lastname@company.co.uk.
Visit https://www.example.com for details or http://subdomain.example.org/page.
Call us at (123) 456-7890, 123-456-7890, or 123.456.7890.
Follow us on social media: #example #ThisIsAHashtag.
"""

# Running the extractors
emails = extract_emails(sample_text)
urls = extract_urls(sample_text)
phone_numbers = extract_phone_numbers(sample_text)
hashtags = extract_hashtags(sample_text)

# Displaying results
print("Extracted Emails:", emails)
print("Extracted URLs:", urls)
print("Extracted Phone Numbers:", phone_numbers)
print("Extracted Hashtags:", hashtags)
