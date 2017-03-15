import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.utils.safestring import SafeString
from django.views import generic

from ..forms.participation_forms import MembershipUpdateForm, OrganizationUpdateForm, \
    RemoveMembershipForm
from ..models.participation import MembershipManager, Organization, Membership, Participant


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


def render_object_membership_set_to_string(organization, template_name=None):
    if template_name is None:
        template_name = 'scheduler/partials/member_list.html'
    membership_set_all = organization.membership_set.all()
    return render_to_string(template_name, {'memberships': membership_set_all})  # the revised table rows / list

def add_organization_member(request, org_pk):
    """renders a modal partial template for adding members to an organization.

    :param request: HTTP request
    :param org_pk: Organization PK to add members into
    :return:
    """
    data = dict()
    context = dict()
    organization = get_object_or_404(Organization, pk=org_pk)

    if request.method == 'POST':
        form = MembershipUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            data['html_member_list'] = render_object_membership_set_to_string(organization)
        else:
            data['form_is_valid'] = False
    else:
        form = MembershipUpdateForm()
    template_name = 'scheduler/partials/add_organization_member.html'
    context.update({'form': form, 'organization': organization})
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def remove_organization_membership(request, pk):
    """ render modal partial template to confirm removal of organization membershp.
        url name: remove_membership
    """
    data = dict()
    context = dict()
    membership = get_object_or_404(Membership, pk=pk)
    organization = membership.organization

    if request.method == 'POST':
        form = RemoveMembershipForm(request.POST)
        if form.is_valid():  # to check CSRF
            membership.delete()
            data['form_is_valid'] = True
            data['html_member_list'] = render_object_membership_set_to_string(organization)
        else:
            data['form_is_valid'] = False
    else:
        form = RemoveMembershipForm()
        template_name = 'scheduler/partials/remove_membership.html'
        context.update({'form': form, 'organization': organization, 'membership': membership, })
        data['html_form'] = render_to_string(template_name, context, request=request)

    return JsonResponse(data)


class OrganizationMembershipListView(generic.ListView):
    """Lists membership for an organization"""
    template_name = 'scheduler/organization_membership.html'
    context_object_name = 'memberships'

    def get_context_data(self, **kwargs):
        context = super(OrganizationMembershipListView, self).get_context_data(**kwargs)
        organization = get_object_or_404(Organization, pk=self.kwargs['pk'])
        organization_dict = {'organization_name': organization.name, 'organization_id': organization.pk, }
        context_json = json.dumps(organization_dict)
        context['organization'] = organization
        context['context_json'] = SafeString(context_json)
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
