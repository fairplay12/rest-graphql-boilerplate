from graphene_django import DjangoObjectType
from jobs.models import Company


class CompanyType(DjangoObjectType):
    class Meta:
        model = Company
