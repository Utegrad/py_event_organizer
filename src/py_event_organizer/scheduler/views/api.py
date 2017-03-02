from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from ..serializers.participation_serializer import ParticipantSerializer, MembershipSerializer
from ..serializers.participation_serializer import OrganizationSerializer, DelegatesSerializer

from ..models.participation import Participant, Membership, Organization, Delegates


class ParticipantApiView(ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer


class OrganizationApiView(ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class MembershipApiView(ModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer


class DelegateApiView(ModelViewSet):
    queryset = Delegates.objects.all()
    serializer_class = DelegatesSerializer
