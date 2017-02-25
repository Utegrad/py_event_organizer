from rest_framework import serializers

from ..models.participation import Participant, Organization, Delegates, Membership


class ParticipantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Participant


class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization


class MembershipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Membership


class DelegatesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Delegates


