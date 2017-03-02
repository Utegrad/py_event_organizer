from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from scheduler.views.api import ParticipantApiView , MembershipApiView, OrganizationApiView, \
    DelegateApiView

router = DefaultRouter()
router.register(r'v1/participants', ParticipantApiView)
router.register(r'v1/memberships', MembershipApiView)
router.register(r'v1/organizations', OrganizationApiView)
router.register(r'v1/deletates', DelegateApiView)

urlpatterns = router.urls


