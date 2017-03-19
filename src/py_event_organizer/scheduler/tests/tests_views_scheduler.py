import random
import string
import sys
import unittest

from django.contrib.auth.models import User
from django.http import Http404
from django.test import RequestFactory, TestCase
from django.urls import reverse

from ..models.participation import Participant, Membership, Organization
from ..views.scheduler import MyManagedOrgsListView, OrganizationMembershipListView, \
    UpdateOrganizationView, UpdateMembershipView, MyOrgsListView, add_organization_member, \
    remove_organization_membership


def random_string():
    return ''.join(random.choice(string.ascii_letters) for i in range(18))


def create_user(email, username=None, password=None):
    name = username if username is not None else random_string()
    pw = password if password is not None else random_string()
    return User.objects.create_user(username=name, password=pw, email=email)


class SchedulerTests(unittest.TestCase):
    pk_arg = None
    anonymous_user = None
    user = None
    factory = None
    participant_1 = None
    participant_2 = None
    organization_1 = None
    organization_2 = None
    membership_1 = None
    membership_2 = None
    auth_username = 'unit_tester'
    auth_password = 'super_secret'
    auth_email = 'unit.tester@nowhere.net'

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
        self.participant_1 = participant_1
        participant_2.save()
        self.participant_2 = participant_2
        org_1 = Organization(name=org_names[0])
        org_2 = Organization(name=org_names[1])
        org_1.save()
        self.organization_1 = org_1
        org_2.save()
        self.organization_2 = org_2
        membership_1 = Membership(role='EDIT', participant=participant_1, organization=org_1)
        membership_2 = Membership(role='VIEW', participant=participant_2, organization=org_1)
        membership_1.save()
        self.membership_1 = membership_1
        membership_2.save()
        self.membership_2 = membership_2

    def setUp(self):
        self.pk_arg = 1
        self.factory = RequestFactory()
        self.set_membership_test_data(first_names=('Joe', 'Betty'),
                                      last_names=('Blow', 'Boop'),
                                      org_names=('Org1', 'Org2'))


class MyOrganizationsViewTests(SchedulerTests):
    def setUp(self):
        super().setUp()
        self.user = create_user(self.auth_email)

    def test_MyManagedOrgsListView_returns_200(self):
        request = self.factory.get(reverse('scheduler:my_managed_orgs',
                                           kwargs={'pk': self.pk_arg}))

        request.user = self.user
        response = MyManagedOrgsListView.as_view()(request, pk=self.pk_arg)
        self.assertEqual(response.status_code, 200)

    def test_MyManagedOrgsListView_has_context_data_objects(self):
        request = self.factory.get(reverse('scheduler:my_managed_orgs',
                                           kwargs={'pk': self.pk_arg}))
        request.user = self.user
        response = MyManagedOrgsListView.as_view()(request, pk=self.pk_arg)
        self.assertGreaterEqual(len(response.context_data['object_list']), 1)

    def test_MyOrgsListView_returns_200(self):
        request = self.factory.get(reverse('scheduler:my_memberships', kwargs={'pk': self.pk_arg}))
        request.user = self.user
        response = MyOrgsListView.as_view()(request, pk=self.pk_arg)
        self.assertEqual(response.status_code, 200)


class MyManagedOrgsListViewTests(TestCase):
    def setUp(self):
        self.password = random_string()
        self.username = random_string()
        self.user = create_user(email='foo@bar.baz', username=self.username, password=self.password)

    def test_MyManagedOrgsListView_context_set(self):
        pk_arg = 1
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('scheduler:my_managed_orgs',
                                           kwargs={'pk': pk_arg}))
        self.assertQuerysetEqual(response.context['my_managed_orgs'], [])


class AddOrganizationMemberTests(SchedulerTests):
    """Tests for the add_organization_member method"""

    def setUp(self):
        super().setUp()
        self.user = create_user(self.auth_email)

    def test_add_organization_member_get_returns_200(self):
        # Setup
        request = self.factory.get(reverse('scheduler:add_member', kwargs={'org_pk': self.pk_arg}))
        request.user = self.user
        # Run
        response = add_organization_member(request, org_pk=self.pk_arg)
        # Assert
        self.assertEqual(response.status_code, 200)

    def test_add_organization_member_status_code_404_with_bad_pk(self):
        bad_pk = sys.maxsize
        request = self.factory.get(reverse('scheduler:add_member', kwargs={'org_pk': bad_pk}))
        request.user = self.user
        with self.assertRaises(Http404):
            response = add_organization_member(request, org_pk=bad_pk)

    def test_add_organization_member_post_returns_200(self):
        """ Test putting the second participant in the second organization created
        by the inherited test class"""
        membership_post_data = {'participant': self.participant_2,
                                'organization': self.organization_2,
                                'role': 'VIEW'}
        request = self.factory.post(reverse('scheduler:add_member',
                                            kwargs={'org_pk': self.pk_arg}, ),
                                    data=membership_post_data)
        request.user = self.user
        response = add_organization_member(request, self.pk_arg)
        self.assertEqual(response.status_code, 200)


class RemoveOrganizationMemberTests(SchedulerTests):
    """ Tests for the remove_organization_member method"""

    def setUp(self):
        super().setUp()
        self.user = create_user(email=self.auth_email)

    def test_remove_organization_member_get_returns_200(self):
        """ Test get request for confirmation to remove membership from organization."""
        request = self.factory.get(reverse('scheduler:remove_membership',
                                           kwargs={'pk': self.membership_2.id}))
        request.user = self.user
        response = remove_organization_membership(request=request, pk=self.membership_2.id)
        self.assertEqual(response.status_code, 200)


class OrganizationMembershipListViewTests(SchedulerTests):
    def setUp(self):
        super().setUp()
        self.user = create_user(email=self.auth_email)

    def test_OrganizationMembershipListView_returns_200(self):
        request = self.factory.get(reverse('scheduler:organization_membership',
                                           kwargs={'pk': self.pk_arg}))
        request.user = self.user
        response = OrganizationMembershipListView.as_view()(request, pk=self.pk_arg)
        self.assertEqual(response.status_code, 200)

    def test_OrganizationMembershipListView_status_code_404_with_bad_pk(self):
        bad_pk = sys.maxsize
        request = self.factory.get(reverse('scheduler:organization_membership',
                                           kwargs={'pk': bad_pk}))
        request.user = self.user
        with self.assertRaises(Http404):
            response = OrganizationMembershipListView.as_view()(request, pk=bad_pk)


class UpdateOrganizationViewTests(SchedulerTests):
    def setUp(self):
        super().setUp()
        self.user = create_user(self.auth_email)

    def test_UpdateMembershipView_returns_200(self):
        request = self.factory.get(reverse('scheduler:update_organization',
                                           kwargs={'pk': self.pk_arg}))
        request.user = self.user
        response = UpdateOrganizationView.as_view()(request, pk=self.pk_arg)
        self.assertEqual(response.status_code, 200)


class UpdateMembershipViewTests(SchedulerTests):
    def setUp(self):
        super().setUp()
        self.user = create_user(self.auth_email)

    def test_UpdateMembershipView_returns_200(self):
        request = self.factory.get(reverse('scheduler:update_membership',
                                           kwargs={'pk': self.pk_arg}))
        request.user = self.user
        response = UpdateMembershipView.as_view()(request, pk=self.pk_arg)
        self.assertEqual(response.status_code, 200)
