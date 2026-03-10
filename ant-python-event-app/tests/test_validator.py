import unittest
from src.validator import validate_attendee

class TestValidator(unittest.TestCase):

    def test_valid_attendee(self):
        attendee = {
            "name": "Sara Palacios",
            "email": "sara@example.com",
            "user_id": "EV-1023",
            "age": 25,
            "ticket_type": "vip"
        }
        self.assertEqual(validate_attendee(attendee), [])

    def test_invalid_email(self):
        attendee = {
            "name": "Juan",
            "email": "juanexample.com",
            "user_id": "EV-0001",
            "age": 20,
            "ticket_type": "general"
        }
        self.assertIn("Invalid email", validate_attendee(attendee))

    def test_underage_attendee(self):
        attendee = {
            "name": "Ana",
            "email": "ana@example.com",
            "user_id": "EV-9876",
            "age": 16,
            "ticket_type": "student"
        }
        self.assertIn("Attendee must be 18 or older", validate_attendee(attendee))

    def test_invalid_user_id_formats(self):
        attendee = {
            "name": "Marco",
            "email": "marco@example.com",
            "user_id": "EV-12A3",
            "age": 30,
            "ticket_type": "general"
        }
        self.assertIn("Invalid user ID", validate_attendee(attendee))

    def test_valid_user_id_formats(self):
        attendee = {
            "name": "Lucia",
            "email": "lucia@example.com",
            "user_id": "EV-1023",
            "age": 28,
            "ticket_type": "vip"
        }
        self.assertNotIn("Invalid user ID", validate_attendee(attendee))

if __name__ == "__main__":
    unittest.main()