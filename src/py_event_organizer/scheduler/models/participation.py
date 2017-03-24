from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from .common import TimeStampedObjectModel, CONTACT_TYPES


class Participant(TimeStampedObjectModel):
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.SET_NULL)
    first_name = models.CharField(max_length=48, blank=False, )
    last_name = models.CharField(max_length=48, blank=True, )
    nick_name = models.CharField(max_length=64, blank=True, )
    prefered_contact_method = models.CharField(max_length=5, choices=CONTACT_TYPES, default='SMS', )
    delegates = models.ManyToManyField('self', through='Delegates',
                                       symmetrical=False,
                                       related_name='related_to', blank=True )
    deferential_delegation = models.BooleanField(help_text= 'only delegates should receive notifications',
                                                 default=False, )
    direct_participant = models.BooleanField(help_text='Participant is a direct participant in the organization events',
                                             default=True)

    @property
    def full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def __str__(self):
        return "{0}".format(self.full_name)


class Organization(TimeStampedObjectModel):
    name = models.CharField(max_length=64)
    members = models.ManyToManyField(Participant, through='Membership', )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('scheduler:update_organization', kwargs={'pk': self.pk})

    def participant_can_edit_membership(self, participant):
        membership = self.membership_set.get(participant=participant)
        role = membership.role
        if role == 'EDIT':
            return True
        else:
            return False


class Membership(TimeStampedObjectModel):
    MEMBER_TYPE = (('EDIT', 'Editor'), ('VIEW', 'Viewer'),)
    # first value is stored in the database, second value is shown on the Django admin UI
    participant = models.ForeignKey(Participant)
    organization = models.ForeignKey(Organization)
    role = models.CharField(max_length=4, choices=MEMBER_TYPE, default='EDIT', )

    def __str__(self):
        return "{0} : {1}".format(self.participant, self.organization)

    def get_absoute_url(self):
        return reverse('scheduler:list_memberhips', kwargs={'pk': self.pk})

    @property
    def member_set_organization_name(self):
        return self.objects.all()[0].organization

    class Meta:
        unique_together = ( ('participant', 'organization'), )


class MembershipManager(models.Manager):
    def get_participant_memberships_by_role(self, participant_id, role):
        memberships = Membership.objects.filter(participant_id=participant_id, role=role)
        return memberships

    def get_participant_memberships(self, participant_id):
        memberships = Membership.objects.filter(participant_id=participant_id)
        return memberships

    def get_participation(self, participant_id, role=None):
        if role is None:
            return self.get_participant_memberships(participant_id)
        else:
            return self.get_participant_memberships_by_role(participant_id, role)



class Delegates(TimeStampedObjectModel):
    participant = models.ForeignKey(Participant, related_name='delegated_from')
    delegate = models.ForeignKey(Participant, related_name='delegated_to')
    organization = models.ForeignKey(Organization, )

    def __str__(self):
        return "{0} => {1} : {2}".format(self.participant, self.delegate, self.organization)

    class Meta:
        verbose_name = "Contact Delegates"
        verbose_name_plural = "Delegates"
        unique_together = ( ('participant', 'delegate', 'organization'), )


