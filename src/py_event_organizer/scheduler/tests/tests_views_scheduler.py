import unittest

from django.test import RequestFactory
from django.test import TestCase, Client
from django.urls import reverse

from ..views.scheduler import MyManagedOrgsListView


class MyOrganizationsViewTests(unittest.TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_MyManagedOrgsListView_returns_200(self):
        request = self.factory.get(reverse('scheduler:my_managed_orgs', kwargs={'pk':1}))
        response = MyManagedOrgsListView.as_view()(request) # TODO: Figure out why this isn't getting kwargs to the view
        self.assertEqual(response.status_code, 200)