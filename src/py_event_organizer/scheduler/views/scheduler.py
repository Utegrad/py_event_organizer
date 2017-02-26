from django.views import generic

from ..models.participation import MembershipManager
# Create your views here.

class MyManagedOrgsListView(generic.ListView):
    template_name = 'scheduler/my_managed_orgs.html'
    context_object_name = 'my_managed_orgs'

    def get_queryset(self):
        mgr = MembershipManager()
        query_set = mgr.get_participant_memberships_by_role(participant_id=self.kwargs['pk'], role='EDIT')
        return query_set

