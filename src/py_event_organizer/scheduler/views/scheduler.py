from django.views import generic
from django.shortcuts import get_object_or_404

from ..models.participation import MembershipManager, Organization, Membership, Participant
from ..forms.participation_forms import MembershipUpdateForm, DelegatesUpdateForm, \
    OrganizationUpdateForm, ParticipantUpdateForm

# Create your views here.

# TODO: View needs to be limited to match pk to logged in user
class MyManagedOrgsListView(generic.ListView):
    template_name = 'scheduler/my_managed_orgs.html'
    context_object_name = 'my_managed_orgs'

    def get_queryset(self):
        mgr = MembershipManager()
        query_set = mgr.get_participant_memberships_by_role(participant_id=self.kwargs['pk'],
                                                            role='EDIT')
        return query_set


class UpdateOrganizationView(generic.UpdateView):
    """Allows for updating properties of an Organization"""
    template_name = 'scheduler/update_organization.html'
    form_class = OrganizationUpdateForm
    model = Organization


class UpdateMembershipView(generic.UpdateView):
    """Doesn't make sense to update a membership outside the
    context of managing an Organization.
    """
    template_name = 'scheduler/update_membership.html'
    form_class = MembershipUpdateForm
    model = Membership


class OrganizationMembershipListView(generic.ListView):
    """Lists membership for an organization"""
    template_name = 'scheduler/organization_membership.html'
    context_object_name = 'memberships'

    def get_context_data(self, **kwargs):
        context = super(OrganizationMembershipListView, self).get_context_data(**kwargs)
        context['organization'] = get_object_or_404(Organization, pk=self.kwargs['pk'])
        return context

    def get_queryset(self):
        organization = get_object_or_404(Organization, pk=self.kwargs['pk'])
        return organization.membership_set.all()

class MyOrgsListView(generic.ListView):
    """Listing of organizations that a participant is a member of"""
    template_name = 'scheduler/my_memberships.html'
    context_object_name = 'my_memberships'

    def get_queryset(self):
        participant = get_object_or_404(Participant, pk=self.kwargs['pk'])
        return Membership.objects.filter(participant=participant)

