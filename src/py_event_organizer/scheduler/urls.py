from django.conf.urls import url
from .views.standard import IndexView as home_page
from .views.scheduler import MyManagedOrgsListView

app_name = 'scheduler'
urlpatterns = [
    url(r'^$', view=home_page.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/managed_orgs/',
        view=MyManagedOrgsListView.as_view(),
        name='my_managed_orgs'),

]