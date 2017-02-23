from django.db import models


# Create your models here.

CONTACT_TYPES = (('SMS', 'Text Message'), ('EMAIL', 'Email'),)

def get_contact_type_value(contact_type):
    return [item[0] for item in CONTACT_TYPES if item[1] == contact_type][0]

class TimeStampedObjectModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, )
    updated_on = models.DateTimeField(auto_now=True, )

    class Meta:
        abstract = True


class Organization(TimeStampedObjectModel):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Participant(TimeStampedObjectModel):
    name = models.CharField(max_length=64, blank=False, )
    prefered_contact_method = models.CharField(max_length=5, choices=CONTACT_TYPES, default='SMS', )

    def __str__(self):
        return "{0}".format(self.name)


class Contact(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, )
    updated_on = models.DateTimeField(auto_now=True, )
    owner = models.ForeignKey('Participant', on_delete=models.PROTECT, blank=False, )
    weight = models.IntegerField(default=0, )

    def __str__(self):
        return "{0} <{1}>".format(self.owner, self.contact_point)

    class Meta:
        abstract = True


class SMS(Contact):
    contact_point = models.CharField(max_length=16, blank=False, )
    type = models.CharField(max_length=3, choices=CONTACT_TYPES, default='SMS',
                            editable=False)

    class Meta:
        verbose_name = "SMS Contact"
        verbose_name_plural = "SMS Contacts"

class Email(Contact):
    contact_point = models.EmailField(max_length=64, blank=False, )
    type = models.CharField(max_length=5, choices=CONTACT_TYPES, default='EMAIL',
                            editable=False)

    class Meta:
        verbose_name = "Email Contact"
        verbose_name_plural = "Email Contacts"



