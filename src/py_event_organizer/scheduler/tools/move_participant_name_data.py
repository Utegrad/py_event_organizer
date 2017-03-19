import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings.local"
application = get_wsgi_application()

from django.contrib.auth.models import User
from scheduler.models.participation import Participant


def transfer_user_name_values(participant):
    participant.user.first_name = participant.first_name
    participant.user.last_name = participant.last_name
    participant.user.full_clean()
    participant.user.save()


def create_user(first_name, last_name):
    password = "babe9237"
    user_name_first = first_name.replace(" ", "")
    user_name_last = last_name.replace(" ", "")
    username = "{0}.{1}".format(user_name_first, user_name_last).lower()
    email = "{0}@{1}".format(username, "nowhere.net")
    user = User.objects.create_user(username=username, email=email, password=password, )
    return user


def main():
    all_participants = Participant.objects.all()
    for participant in all_participants:
        if participant.user is None:
            msg = "Creating user for {0}".format(participant.full_name)
            print(msg)
            create_user_for_participant(participant)
        msg = "Copying first and last name from Participant to User for {0}".format(participant.full_name)
        print(msg)
        transfer_user_name_values(participant=participant)
    print("Done")


def create_user_for_participant(participant):
    user = create_user(first_name=participant.first_name, last_name=participant.last_name)
    participant.user = user
    participant.full_clean()
    participant.save()


if __name__ == '__main__':
    try:
        main()
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nStopped")
        sys.exit(0)
