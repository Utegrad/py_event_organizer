from django.conf.urls import url
from .views.standard import IndexView as home_page

app_name = 'scheduler'
urlpatterns = [
    url(r'^$', view=home_page.as_view(), name='index'),
]