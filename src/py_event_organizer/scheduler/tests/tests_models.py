import unittest
from django.test import TestCase

from ..models import ContactType, Email, SMS, Contact

# Create your tests here.

class SMSTestCase(TestCase):
    fixtures = [ 'contacttypes.json', ]

    def setUp(self):
        pass

    def test_sms_type_is_sms(self):
        """
        Checks that an SMS record has a type of SMS
        :return:
        """
        # get an SMS record
        sms_record = SMS.objects.all()[0]

