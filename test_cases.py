# test_cases.py

# Import the extraction functions from extractor.py
from extractor import extract_emails, extract_urls, extract_phone_numbers, extract_hashtags

def run_tests():
    sample_texts = [
        # Valid cases
        ("Valid Emails", "user@example.com, contact@domain.net"),
        ("Valid URLs", "Check this: https://example.com and http://sub.example.org"),
        ("Valid Phones", "Call me at (123) 456-7890 or 123-456-7890"),
        ("Valid Hashtags", "Follow #coding and #PythonTips"),
        
        # Edge cases
        ("Invalid Emails", "user@.com, @example.com, user@com"),
        ("Invalid URLs", "www.example.com, htp://wrong.com, http:/bad.com"),
        ("Invalid Phones", "1234567, 12-34-5678, phone123"),
        ("Invalid Hashtags", "#123, #hash tag, hashtag#"),
        
        # Empty case
        ("Empty Text", "")
    ]

    for case, text in sample_texts:
        print(f"\n🔹 Testing: {case}")
        print("Emails:", extract_emails(text))
        print("URLs:", extract_urls(text))
        print("Phone Numbers:", extract_phone_numbers(text))
        print("Hashtags:", extract_hashtags(text))
        print("-" * 50)

# Run tests
if __name__ == "__main__":
    run_tests()
