from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey('accounts.Employer', related_name='companies')

    def __str__(self):
        return self.name
