from rest_framework import serializers

from ..models.participation import Participant, Organization, Delegates, Membership


class ParticipantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Participant
        fields = ('name', 'prefered_contact_method', )


class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = ('name', )


class MembershipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Membership
        fields = '__all__'


class DelegatesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Delegates
        fields = '__all__'


