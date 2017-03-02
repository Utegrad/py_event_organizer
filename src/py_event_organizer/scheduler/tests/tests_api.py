import unittest

from django.test import RequestFactory
from django.test import TestCase, Client
from django.urls import reverse

from ..views.api import DelegateApiView, ParticipantApiView, OrganizationApiView, MembershipApiView


class ApiViewTests(unittest.TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    @unittest.skip("Don't know how to make work it DefaultRouter")
    def test_api_participant_list_200_status_code(self):
        request = self.factory.get(reverse('api:participant_list'), content_type='application/json')
        response = ParticipantApiView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    @unittest.skip("Don't know how to make work it DefaultRouter")
    def test_api_organization_list_200_status_code(self):
        request = self.factory.get(reverse('api:organization_list'), content_type='application/json')
        response = OrganizationApiView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    @unittest.skip("Don't know how to make work it DefaultRouter")
    def test_api_membership_list_200_status_code(self):
        request = self.factory.get(reverse('api:membership_list'), content_type='application/json')
        response = MembershipApiView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    @unittest.skip("Don't know how to make work it DefaultRouter")
    def test_api_delegate_list_200_status_code(self):
        request = self.factory.get(reverse('api:delegate_list'), content_type='application/json')
        response = DelegateApiView.as_view()(request)
        self.assertEqual(response.status_code, 200)

