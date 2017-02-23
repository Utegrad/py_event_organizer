from django.db import models

from .common import TimeStampedObjectModel, CONTACT_TYPES


class Participant(TimeStampedObjectModel):
    name = models.CharField(max_length=64, blank=False, )
    prefered_contact_method = models.CharField(max_length=5, choices=CONTACT_TYPES, default='SMS', )

    def __str__(self):
        return "{0}".format(self.name)


class Organization(TimeStampedObjectModel):
    name = models.CharField(max_length=64)
    members = models.ManyToManyField(Participant, through='Membership')

    def __str__(self):
        return self.name


class Membership(TimeStampedObjectModel):
    MEMBER_TYPE = (('EDIT', 'Editor'), ('VIEW', 'Viewer'),)
    participant = models.ForeignKey(Participant)
    organization = models.ForeignKey(Organization)
    role = models.CharField(max_length=4, choices=MEMBER_TYPE, default='EDIT', )

    def __str__(self):
        return "{0} : {1}".format(self.participant, self.organization)

