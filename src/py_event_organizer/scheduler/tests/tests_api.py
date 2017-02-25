import unittest

from django.test import RequestFactory
from django.test import TestCase, Client
from django.urls import reverse

from ..views.api import DelegateApiView, ParticipantApiView, OrganizationApiView, MembershipApiView


class ApiViewTests(unittest.TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_api_participant_list_200_status_code(self):
        request = self.factory.get(reverse('api:participant_list'))
        response = ParticipantApiView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_api_organization_list_200_status_code(self):
        request = self.factory.get(reverse('api:organization_list'))
        response = OrganizationApiView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_api_membership_list_200_status_code(self):
        request = self.factory.get(reverse('api:membership_list'))
        response = MembershipApiView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_api_delegate_list_200_status_code(self):
        request = self.factory.get(reverse('api:delegate_list'))
        response = DelegateApiView.as_view()(request)
        self.assertEqual(response.status_code, 200)

