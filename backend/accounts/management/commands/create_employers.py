from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from accounts.models import Employer


class Command(BaseCommand):
    help = "create random users for populate db"

    def handle(self, *args, **kwargs):

        for i in range(1, 101):
            user = User.objects.create(
                first_name="user_employer_" + str(i),
                last_name="nvm" + str(i),
                username="username_employer_" + str(i),
                email="employer_email_" + str(i) + "@example.com"
            )
            Employer.objects.create(
                is_super_employer=True,
                user=user
            )
