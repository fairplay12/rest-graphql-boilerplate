from django.core.management.base import BaseCommand

from accounts.models import Employee, Employer


class Command(BaseCommand):
    help = "create random users for populate db"

    def handle(self, *args, **kwargs):
        for i in range(10):
            print(i)
