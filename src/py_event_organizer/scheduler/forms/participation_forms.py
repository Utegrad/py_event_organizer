from django.forms import ModelForm
from ..models.participation import Organization, Participant, Membership, Delegates


class OrganizationUpdateForm(ModelForm):

    class Meta:
        model = Organization
        fields = ('name', )


class MembershipUpdateForm(ModelForm):

    class Meta:
        model = Membership
        fields = ('participant', 'organization', 'role',)


class ParticipantUpdateForm(ModelForm):

    class Meta:
        model = Participant
        fields = ('first_name', 'last_name', 'nick_name', 'prefered_contact_method',
                  'deferential_delegation',)


class DelegatesUpdateForm(ModelForm):

    class Meta:
        model = Delegates
        fields = ('participant', 'delegate', 'organization', )


