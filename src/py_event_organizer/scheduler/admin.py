from django.contrib import admin

# Register your models here.
from .models.contacts import SMS, Email
from .models.partipation import Participant, Organization

my_models = [Organization, SMS, Email, Participant]

admin.site.register(my_models)

