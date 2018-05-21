import graphene

from api.graphql.types.accounts import EmployeeType, EmployerType
from accounts.models import Employee, Employer


class EmployeeQuery(graphene.ObjectType):
    employees = graphene.List(EmployeeType)
    employee = graphene.Field(EmployeeType, id=graphene.Int())

    def resolve_employees(self, info):
        return Employee.objects.all()

    def resolve_employee(self, info, id):
        if Employee.objects.filter(id=id).exists():
            return Employee.objects.get(id=id)
        return None


class EmployerQuery(graphene.ObjectType):
    employers = graphene.List(EmployerType)
    employer = graphene.Field(EmployerType, id=graphene.Int())

    def resolve_employers(self, info):
        return Employer.objects.all()

    def resolve_employer(self, info, id):
        if Employer.objects.filter(id=id).exists():
            return Employer.objects.get(id=id)
        return None
