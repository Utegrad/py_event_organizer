from django.db import models

from .common import CONTACT_TYPES, get_contact_type_value

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