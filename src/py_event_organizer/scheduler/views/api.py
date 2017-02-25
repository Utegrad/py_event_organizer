from rest_framework.generics import ListAPIView

from ..serializers.participation_serializer import ParticipantSerializer, MembershipSerializer
from ..serializers.participation_serializer import OrganizationSerializer, DelegatesSerializer

from ..models.participation import Participant, Membership, Organization, Delegates


class ParticipantApiView(ListAPIView):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer


class OrganizationApiView(ListAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class MembershipApiView(ListAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class DelegateApiView(ListAPIView):
    queryset = Delegates.objects.all()
    serializer_class = DelegatesSerializer
