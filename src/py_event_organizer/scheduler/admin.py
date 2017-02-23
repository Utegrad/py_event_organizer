from django.contrib import admin

# Register your models here.
from .models import SMS, Email, Participant, Organization


my_models = [Organization, SMS, Email, Participant]

admin.site.register(my_models)

