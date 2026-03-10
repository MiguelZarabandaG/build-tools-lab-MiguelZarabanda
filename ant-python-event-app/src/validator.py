import re

VALID_TICKETS = {"general", "vip", "student"}


def is_valid_email(email: str) -> bool:
    pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
    return re.match(pattern, email) is not None


def is_valid_user_id(user_id: str) -> bool:
    pattern = r"^EV-\d{4}$"
    return isinstance(user_id, str) and re.match(pattern, user_id) is not None

def validate_attendee(attendee: dict) -> list:
    errors = []

    if not attendee.get("name") or not attendee["name"].strip():
        errors.append("Invalid name")

    if not is_valid_email(attendee.get("email", "")):
        errors.append("Invalid email")

    if not is_valid_user_id(attendee.get("user_id", "")):
        errors.append("Invalid user ID")

    age = attendee.get("age")
    if not isinstance(age, int) or age < 18:
        errors.append("Attendee must be 18 or older")

    if attendee.get("ticket_type") not in VALID_TICKETS:
        errors.append("Invalid ticket type")

    return errors