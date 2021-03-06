from django.conf.urls import url
from .views.standard import IndexView as home_page
from .views.scheduler import MyManagedOrgsListView
from .views.scheduler import UpdateOrganizationView, UpdateMembershipView, \
    OrganizationMembershipListView, MyOrgsListView, add_organization_member, \
    remove_organization_membership

app_name = 'scheduler'
urlpatterns = [
    url(r'^$', view=home_page.as_view(), name='index'),

    url(r'^participant/managed_orgs/', view=MyManagedOrgsListView.as_view(),
        name='my_managed_orgs'),
    url(r'^participant/membership/', view=MyOrgsListView.as_view(), name='my_memberships'),

    url(r'^membership/(?P<pk>\d+)/update/', view=UpdateMembershipView.as_view(),
        name='update_membership'),
    url(r'^membership/(?P<pk>\d+)/remove/', view=remove_organization_membership, name='remove_membership'),

    url('^organization/(?P<pk>\d+)/members/', view=OrganizationMembershipListView.as_view(),
        name='organization_membership'),
    url(r'^organization/(?P<pk>\d+)/update/', view=UpdateOrganizationView.as_view(), name='update_organization'),
    url(r'^organization/(?P<org_pk>\d+)/add_member/', view=add_organization_member, name='add_member'),

]
