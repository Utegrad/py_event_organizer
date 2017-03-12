from django.http import JsonResponse
from django.template.loader import render_to_string
from django.utils.safestring import SafeString
from django.views import generic
from django.shortcuts import get_object_or_404
import json

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


class ObjectCrudFormObject:
    """class created to hold arguments for save_organization_membership function"""
    form = None
    template_name = None
    object_id = None

    def __init__(self, form, template_name, object_id):
        self.form = form
        self.template_name = template_name
        self.object_id = object_id


def save_organization_membership(request, crud_form):
    data = dict()
    context = dict()
    organization = get_object_or_404(Organization, pk=crud_form.object_id)

    if request.method == 'POST':
        if crud_form.form.is_valid():
            crud_form.form.save()
            data['form_is_valid'] = True
            membership = organization.membership_set.all()
            data['html_member_list'] = render_to_string('scheduler/partials/member_list.html',
                                                        {'memberships': membership})  # the revised table rows / list
        else:
            data['form_is_valid'] = False

    context.update({'form': crud_form.form, 'organization': organization})
    data['html_form'] = render_to_string(crud_form.template_name, context, request=request)
    return JsonResponse(data)


def add_organization_member(request, org_pk):
    """renders a modal partial template for adding members to an organization.

    :param request: HTTP request
    :param org_pk: Organization PK to add members into
    :return:
    """

    if request.method == 'POST':
        form = MembershipUpdateForm(request.POST)
    else:
        form = MembershipUpdateForm()

    crud_form = ObjectCrudFormObject(form,
                                     'scheduler/partials/add_organization_member.html', org_pk)
                                        # the form
    return save_organization_membership(request, crud_form)


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
