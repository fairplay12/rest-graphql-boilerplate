from django.db import models


class Business(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey('accounts.Employer', related_name='companies')
    business = models.ForeignKey(
        Business,
        related_name='companies',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name
