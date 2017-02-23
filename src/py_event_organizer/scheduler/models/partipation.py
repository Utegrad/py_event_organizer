from django.db import models

from .common import TimeStampedObjectModel, CONTACT_TYPES


class Participant(TimeStampedObjectModel):
    name = models.CharField(max_length=64, blank=False, )
    prefered_contact_method = models.CharField(max_length=5, choices=CONTACT_TYPES, default='SMS', )
    delegates = models.ManyToManyField('self', through='Delegates',
                                       symmetrical=False,
                                       related_name='related_to', blank=True )

    def __str__(self):
        return "{0}".format(self.name)


class Organization(TimeStampedObjectModel):
    name = models.CharField(max_length=64)
    members = models.ManyToManyField(Participant, through='Membership', )

    def __str__(self):
        return self.name


class Membership(TimeStampedObjectModel):
    MEMBER_TYPE = (('EDIT', 'Editor'), ('VIEW', 'Viewer'),)
    participant = models.ForeignKey(Participant)
    organization = models.ForeignKey(Organization)
    role = models.CharField(max_length=4, choices=MEMBER_TYPE, default='EDIT', )

    def __str__(self):
        return "{0} : {1}".format(self.participant, self.organization)

    class Meta:
        unique_together = ( ('participant', 'organization'), )


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


