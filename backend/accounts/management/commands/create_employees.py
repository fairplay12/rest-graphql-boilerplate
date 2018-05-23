from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from accounts.models import Employee
from jobs.models import Company


class Command(BaseCommand):
    help = "create employees"

    def handle(self, *args, **kwargs):
        for i in range(1, 1001):
            if i % 100 == 0:
                company = Company.objects.get(id=100)
            else:
                company = Company.objects.get(id=i%100)
            user = User.objects.create(
                first_name="user_employee_" + str(i),
                last_name="nvm" + str(i),
                username="username_employee_" + str(i),
                email="employee_email_" + str(i) + "@example.com"
            )
            Employee.objects.create(
                experience=i%10,
                user=user,
                company=company
            )
