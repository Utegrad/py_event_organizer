import unittest

from django.test import RequestFactory
from django.test import TestCase, Client
from django.urls import reverse

from ..views.standard import IndexView


class IndexViewTests(unittest.TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_IndexView_returns_200(self):
        request = self.factory.get(reverse('scheduler:index'))
        response = IndexView.as_view()(request)
        self.assertEqual(response.status_code, 200)


class IndexViewContentTests(TestCase):

    def test_IndexView_content_canary(self):
        response = self.client.get(reverse('scheduler:index'))
        self.assertContains(response, "TestCase canary")

