from django.conf.urls import url

from scheduler.views.api import ParticipantApiView as participant_list, \
    MembershipApiView as membership_list, OrganizationApiView as organization_list, \
    DelegateApiView as delegate_list


urlpatterns = [
    url(r'^participants', view=participant_list.as_view(), name='participant_list'),
    url(r'^memberships', view=membership_list.as_view(), name='membership_list'),
    url(r'^organizations', view=organization_list.as_view(), name='organization_list'),
    url(r'^delegates', view=delegate_list.as_view(), name='delegate_list'),
]