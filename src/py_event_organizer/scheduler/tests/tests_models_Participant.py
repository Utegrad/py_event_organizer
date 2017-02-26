import unittest
from unittest.mock import MagicMock

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
        self.membership_1 = Membership(role='EDIT', participant=self.participant_1,
                                  organization=self.organization_1)
        self.membership_2 = Membership(role='VIEW', participant=self.participant_1,
                                  organization=self.organization_2)
        self.membership_1.save()
        self.membership_2.save()


    def test_memberships_where_editor(self):
        mgr = MembershipManager()
        membership = mgr.get_participant_memberships_by_role(participant_id=self.participant_1,
                                                             role='EDIT')
        self.assertGreaterEqual(len(membership), 1)



