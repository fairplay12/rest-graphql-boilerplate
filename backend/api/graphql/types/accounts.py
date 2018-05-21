from graphene_django import DjangoObjectType
from accounts.models import Employee, Employer


class EmployeeType(DjangoObjectType):
    class Meta:
        model = Employee


class EmployerType(DjangoObjectType):
    class Meta:
        model = Employer
