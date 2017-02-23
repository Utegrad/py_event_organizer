from django.db import models


# Create your models here.
class TimeStampedObjectModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, )
    updated_on = models.DateTimeField(auto_now=True, )

    class Meta:
        abstract = True


class Organization(TimeStampedObjectModel):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class ContactType(TimeStampedObjectModel):
    CONTACT_TYPES = ( ('SMS', 'Text Message'), ('EMAIL', 'Email'), )
    type = models.CharField( max_length=5, choices=CONTACT_TYPES, default='SMS',
                             unique=True, )
    #
    ''' TODO: changed model definition to use choices.
    '''

    def __str__(self):
        display = [item[1] for item in self.CONTACT_TYPES if self.type in item]
        return "{0}".format(display[0])


class Participant(TimeStampedObjectModel):
    name = models.CharField(max_length=64, blank=False, )
    prefered_contact_method = models.ForeignKey('ContactType', on_delete=models.PROTECT, )

    def __str__(self):
        return "{0}".format(self.name)


class Contact(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, )
    updated_on = models.DateTimeField(auto_now=True, )
    contact_point = models.CharField(max_length=64, blank=False)
    owner = models.ForeignKey('Participant', on_delete=models.PROTECT, blank=True, )
    weight = models.IntegerField(default=0, )
    type = models.ForeignKey('ContactType', on_delete=models.PROTECT, blank=True, )
    contact_point = models.CharField(max_length=16, blank=False, )

    def __str__(self):
        return "{0} : {1}".format(self.owner, self.contact_point)

    class Meta:
        abstract = True

def get_contact_type(contact_type):
    return ContactType.objects.filter(type=contact_type)

class SMS(Contact):
    contact_point = models.CharField(max_length=16, blank=False, )

    class Meta:
        verbose_name = "SMS Contact"
        verbose_name_plural = "SMS Contacts"

class Email(Contact):
    contact_point = models.EmailField(max_length=64, blank=False, )

    class Meta:
        verbose_name = "Email Contact"
        verbose_name_plural = "Email Contacts"



