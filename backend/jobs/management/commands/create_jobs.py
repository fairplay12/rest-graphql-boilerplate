from django.core.management.base import BaseCommand

from jobs.models import Business, Company
from accounts.models import Employer


class Command(BaseCommand):
    help = 'create businesses and companies'

    def handle(self, *args, **kwargs):
        for i in range(1, 11):
            Business.objects.create(
                name="business_" + str(i)
            )

        for i in range(1, 101):
            if i%10 == 0:
                business = Business.objects.get(id=10)
            else:
                business = Business.objects.get(id=i%10)

            Company.objects.create(
                name="company_" + str(i),
                owner=Employer.objects.get(id=i),
                business=business
            )
