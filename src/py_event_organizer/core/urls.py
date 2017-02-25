from django.conf.urls import url

from scheduler.views import IndexView as scheduler_index


urlpatters = [
    url(r'^$', view=scheduler_index.as_view()),
]