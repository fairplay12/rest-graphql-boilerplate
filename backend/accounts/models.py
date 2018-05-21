from django.db import models
from django.contrib.auth.models import User


# user-model superstructures
class Employee(models.Model):
    user = models.OneToOneField(User, related_name='employee')
    experience = models.PositiveSmallIntegerField(default=0)
    company = models.ForeignKey(
        'jobs.Company',
        related_name='employees',
        null=True,
        blank=True
    )

    def __str__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)


class Employer(models.Model):
    user = models.OneToOneField(User, related_name='employer')
    is_super_employer = models.BooleanField(default=False)

    def __str__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)
