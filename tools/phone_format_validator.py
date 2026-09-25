"""
phone_format_validator.py - Validates that contact telephone number conforms to E.164 international standard
"""
import sys
import json


def validate_phone_e164(phone_number: str):
    import re
    cleaned = phone_number.strip()
    valid = bool(re.match(r"^\+[1-9]\d{1,14}$", cleaned))
    return {"valid_e164": valid, "phone": cleaned, "status": "VALID" if valid else "INVALID_PHONE_FORMAT"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "phone-format-validator"}))
