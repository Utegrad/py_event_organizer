from django.forms import ModelForm, HiddenInput
from ..models.participation import Organization, Participant, Membership, Delegates


class OrganizationUpdateForm(ModelForm):
    class Meta:
        model = Organization
        fields = ('name', )


class OrganizationMembershipUpdateForm(ModelForm):
    """
    Update an Organization's membership.
    For use when the Organization value is known and set in the view with the initial dict()
    """
    class Meta:
        model = Membership
        fields = ('participant', 'organization', 'role',)
        widgets = {'organization': HiddenInput, }


class RemoveMembershipForm(ModelForm):
    class Meta:
        model = Membership
        fields = []


class ParticipantUpdateForm(ModelForm):
    class Meta:
        model = Participant
        fields = ('first_name', 'last_name', 'nick_name', 'prefered_contact_method',
                  'deferential_delegation',)


class DelegatesUpdateForm(ModelForm):
    class Meta:
        model = Delegates
        fields = ('participant', 'delegate', 'organization', )


