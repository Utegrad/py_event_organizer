from django.conf.urls import url
from django.contrib.auth.views import logout, login
from scheduler.views.standard import IndexView as scheduler_index

urlpatterns = [
    url(r'^$', view=scheduler_index.as_view(), name='index'),
    url(r'^login/$', view=login, name='login'),
    url(r'^logout/$', view=logout, name='logout'),
]