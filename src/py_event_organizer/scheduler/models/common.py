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