import unittest

from django.test import RequestFactory
from django.test import TestCase, Client
from django.urls import reverse

from ..views.scheduler import MyManagedOrgsListView
from ..models.participation import Participant, Membership, Organization, Delegates


class MyOrganizationsViewTests(unittest.TestCase):

    def setUp(self):
        self.pk_arg = 1
        self.factory = RequestFactory()

    def test_MyManagedOrgsListView_returns_200(self):
        request = self.factory.get(reverse('scheduler:my_managed_orgs', kwargs={'pk':self.pk_arg}))
        response = MyManagedOrgsListView.as_view()(request, pk=self.pk_arg)
        self.assertEqual(response.status_code, 200)

    def test_MyManagedOrgsListView_has_context_data_objects(self):
        self.set_membership_test_data(first_names=('Joe', 'Betty'),
                                      last_names=('Blow', 'Boop'),
                                      org_names=('Org1', 'Org2'))
        request = self.factory.get(reverse('scheduler:my_managed_orgs', kwargs={'pk': self.pk_arg}))
        response = MyManagedOrgsListView.as_view()(request, pk=self.pk_arg)
        self.assertGreaterEqual(len(response.context_data['object_list']), 1)

    def set_membership_test_data(self, first_names, last_names, org_names):
        """Saves a couple of participant, organizaton, and membership object to test against

            Creates two participant, organization, and membership objects to test against

        :param first_names: tuple to set first name values on participant objects
        :param last_names: tuple to set last name values on participant objects
        :param org_names: tuple to set a pair of organization objects
        :return: None
        """
        participant_1 = Participant(first_name=first_names[0], last_name=last_names[0], )
        participant_2 = Participant(first_name=first_names[1], last_name=last_names[1], )
        participant_1.save()
        participant_2.save()
        org_1 = Organization(name=org_names[0])
        org_2 = Organization(name=org_names[1])
        org_1.save()
        org_2.save()
        membership_1 = Membership(role='EDIT', participant=participant_1, organization=org_1)
        membership_2 = Membership(role='VIEW', participant=participant_2, organization=org_1)
        membership_1.save()
        membership_2.save()


class MyManagedOrgsListViewTests(TestCase):

    def test_MyManagedOrgsListView_context_set(self):
        pk_arg = 1
        response = self.client.get(reverse('scheduler:my_managed_orgs', kwargs={'pk': pk_arg}))
        self.assertQuerysetEqual(response.context['my_managed_orgs'], [])

