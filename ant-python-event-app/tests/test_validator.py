import unittest
from src.validator import validate_attendee

class TestValidator(unittest.TestCase):

    def test_valid_attendee(self):
        attendee = {
            "name": "Sara Palacios",
            "email": "sara@example.com",
            "registration_code": "EV-1023",
            "age": 25,
            "ticket_type": "vip"
        }
        self.assertEqual(validate_attendee(attendee), [])

    def test_invalid_email(self):
        attendee = {
            "name": "Juan",
            "email": "juanexample.com",
            "registration_code": "EV-0001",
            "age": 20,
            "ticket_type": "general"
        }
        self.assertIn("Invalid email", validate_attendee(attendee))

    def test_underage_attendee(self):
        attendee = {
            "name": "Ana",
            "email": "ana@example.com",
            "registration_code": "EV-9876",
            "age": 16,
            "ticket_type": "student"
        }
        self.assertIn("Attendee must be 18 or older", validate_attendee(attendee))

    def test_invalid_registration_code_formats(self):
        invalid_codes = ["EV1023", "EV-12", "EV-ABCDE", "AB-1234"]

        for code in invalid_codes:
            attendee = {
                "name": "Marco",
                "email": "marco@example.com",
                "registration_code": code,
                "age": 30,
                "ticket_type": "general"
            }
            self.assertIn("Invalid registration code", validate_attendee(attendee))

    def test_valid_registration_code_formats(self):
        valid_codes = ["EV-1023", "EV-0001", "EV-9876"]

        for code in valid_codes:
            attendee = {
                "name": "Lucia",
                "email": "lucia@example.com",
                "registration_code": code,
                "age": 28,
                "ticket_type": "vip"
            }
            self.assertNotIn("Invalid registration code", validate_attendee(attendee))

if __name__ == "__main__":
    unittest.main()