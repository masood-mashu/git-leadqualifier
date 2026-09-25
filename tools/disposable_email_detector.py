"""
disposable_email_detector.py - Detects temporary disposable email domains (e.g. mailinator, tempmail, guerrilla) in lead submissions
"""
import sys
import json


def detect_disposable_email(email_address: str):
    email_lower = email_address.lower().strip()
    disposable_domains = ["mailinator.com", "tempmail.com", "guerrillamail.com", "10minutemail.com", "trashmail.com"]
    domain = email_lower.split("@")[-1] if "@" in email_lower else ""
    is_disposable = domain in disposable_domains
    is_corporate = not (is_disposable or domain in ["gmail.com", "yahoo.com", "hotmail.com"])
    return {"corporate_lead": is_corporate, "is_disposable": is_disposable, "domain": domain, "status": "APPROVED" if is_corporate else "CONSUMER_OR_DISPOSABLE"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "disposable-email-detector"}))
