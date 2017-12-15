import unittest
from django.db.utils import DataError

from .tests_views_scheduler import random_string
from ..models.participation import Participant, Organization, Membership, MembershipManager


class ParticipantTestCases(unittest.TestCase):
    def setUp(self):
        pass

    def test_full_name_from_first_and_last_name(self):
        first = "Joe"
        last = "Blow"
        first_last = " ".join([first, last])
        participant = Participant(first_name=first, last_name=last, )
        self.assertEqual(participant.full_name, first_last)
        self.assertEqual(participant.__str__(), first_last)


class OrganizationTestCases(unittest.TestCase):
    def setUp(self):
        self.org_name = 'organization 1'
        self.org = Organization(name=self.org_name)
        self.org.save()

    def test_organization_name_matches(self):
        self.assertEqual(self.org.__str__(), self.org_name)


class MembershipTestCases(unittest.TestCase):

    def setUp(self):
        self.participant_1 = Participant(first_name="P1", last_name="Editor", )
        self.participant_1.save()
        self.participant_2 = Participant(first_name="P2", last_name="Viewer", )
        self.participant_2.save()
        self.organization_1 = Organization(name="Org1", )
        self.organization_1.save()
        self.organization_2 = Organization(name="Org2", )
        self.organization_2.save()
        self.p1_membership_1 = Membership(role='EDIT', participant=self.participant_1,
                                          organization=self.organization_1)
        self.p1_membership_2 = Membership(role='VIEW', participant=self.participant_1,
                                          organization=self.organization_2)
        self.p2_membership_1 = Membership(role='VIEW', participant=self.participant_2,
                                          organization=self.organization_1)
        self.p1_membership_1.save()
        self.p1_membership_2.save()
        self.p2_membership_1.save()

        self.p2_membership_count = 1
        self.p1_membership_count = 2
        self.p1_editor_count = 1
        self.p2_editor_count = 0

    def test_memberships_where_editor(self):
        mgr = MembershipManager()
        membership = mgr.get_participant_memberships_by_role(participant_id=self.participant_1,
                                                             role='EDIT')
        self.assertGreaterEqual(len(membership), 1)

    def test_memberships_all(self):
        mgr = MembershipManager()
        p1_membership = mgr.get_participant_memberships(participant_id=self.participant_1)
        p2_membership = mgr.get_participant_memberships(participant_id=self.participant_2)
        self.assertEqual(len(p1_membership), self.p1_membership_count)
        self.assertEqual(len(p2_membership), self.p2_membership_count)

    def test_get_all_participation(self):
        mgr = MembershipManager()
        p1_all_memberships = mgr.get_participation(self.participant_1)
        p2_all_memberships = mgr.get_participation(self.participant_2)
        self.assertEqual(len(p1_all_memberships), self.p1_membership_count)
        self.assertEqual(len(p2_all_memberships), self.p2_membership_count)

    def test_get_all_participation_editor_count(self):
        mgr = MembershipManager()
        p1_edit_memberships = mgr.get_participation(self.participant_1, 'EDIT')
        p2_edit_memberships = mgr.get_participation(self.participant_2, 'EDIT')
        self.assertEqual(len(p1_edit_memberships), self.p1_editor_count)
        self.assertEqual(len(p2_edit_memberships), self.p2_editor_count)

    def test_membership_created_with_DataError(self):
        """Trying to create a membership with an invalid role"""
        participant = Participant.objects.create(last_name=random_string())
        organization = Organization.objects.create(name=random_string())
        with self.assertRaises(DataError):
            membership = Membership.objects.create(participant=participant,
                                                   organization=organization,
                                                   role='GARBAGE')


class OrganizationPermissionTestCases(unittest.TestCase):

    def test_participant_can_edit(self):
        participant = Participant.objects.create(last_name=random_string())
        organization = Organization.objects.create(name=random_string())
        membership = Membership.objects.create(participant=participant,
                                               organization=organization,
                                               role='EDIT')
        can_edit = organization.participant_can_edit_membership(participant)
        self.assertTrue(can_edit)

    def test_participant_can_not_edit(self):
        participant = Participant.objects.create(last_name=random_string())
        organization = Organization.objects.create(name=random_string())
        membership = Membership.objects.create(participant=participant,
                                               organization=organization,
                                               role='VIEW')
        can_edit = organization.participant_can_edit_membership(participant)
        self.assertFalse(can_edit)

    def test_Member_can_edit_organization_membership(self):
        participant = Participant.objects.create(last_name=random_string())
        organization = Organization.objects.create(name=random_string())
        membership = Membership.objects.create(participant=participant,
                                               organization=organization,
                                               role='EDIT')
        self.assertTrue(membership.participant_is_organization_editor)

    def test_Member_can_not_edit_organization_membership(self):
        participant = Participant.objects.create(last_name=random_string())
        organization = Organization.objects.create(name=random_string())
        membership = Membership.objects.create(participant=participant,
                                               organization=organization,
                                               role='VIEW')
        self.assertFalse(membership.participant_is_organization_editor)
