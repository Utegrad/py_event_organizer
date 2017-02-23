import unittest
from django.test import TestCase

from  ..models.common import CONTACT_TYPES, get_contact_type_value

class ContactTypeTests(unittest.TestCase):

    def test_get_email_contact_value(self):
        self.assertEqual(get_contact_type_value("Email"), "EMAIL")

    def test_get_sms_contact_value(self):
        self.assertEqual(get_contact_type_value("Text Message"), "SMS")

