from django.contrib import admin

# Register your models here.
from .models.contacts import SMS, Email
from .models.participation import Participant, Organization, Membership, Delegates

my_models = [Organization, SMS, Email, Participant, Membership, Delegates]

admin.site.register(my_models)

