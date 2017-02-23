import unittest
from django.test import TestCase
from django.core.exceptions import ValidationError

from ..models import Email, Participant

class EmailTestCase(unittest.TestCase):

    def test_email_type_is_email(self):
        instance = Email(contact_point="someone@somewhere.com")
        self.assertEqual(instance.type, "EMAIL")

    def test_bad_email_raises_validation_error(self):
        participant = Participant(name="Blah")
        email_contact = Email(contact_point="wrong", owner=participant)
        with self.assertRaises(ValidationError):
            email_contact.clean_fields()




