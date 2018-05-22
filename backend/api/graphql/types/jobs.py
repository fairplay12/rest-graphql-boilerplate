from graphene_django import DjangoObjectType
from jobs.models import Company, Business


class CompanyType(DjangoObjectType):
    class Meta:
        model = Company


class BusinessType(DjangoObjectType):
    class Meta:
        model = Business
