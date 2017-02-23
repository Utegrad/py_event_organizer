import unittest
from django.test import TestCase

from ..models.contacts import SMS

# Create your tests here.

class SMSTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_sms_type_is_sms(self):
        """
        Checks that an SMS record has a type of SMS
        :return:
        """
        # get an SMS record
        instance = SMS(contact_point="8005551212")
        self.assertEqual(instance.type, "SMS")





