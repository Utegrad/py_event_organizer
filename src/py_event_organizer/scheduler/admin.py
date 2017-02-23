from django.contrib import admin

# Register your models here.
from .models import ContactType, SMS, Email, Participant, Organization


my_models = [Organization, ContactType, SMS, Email, Participant]

admin.site.register(my_models)

