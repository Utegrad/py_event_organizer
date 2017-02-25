from django.conf.urls import url

from scheduler.views.standard import IndexView as scheduler_index

urlpatterns = [
    url(r'^$', view=scheduler_index.as_view(), name='index'),
]