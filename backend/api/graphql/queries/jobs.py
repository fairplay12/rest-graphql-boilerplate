import graphene

from api.graphql.types.jobs import CompanyType, BusinessType
from jobs.models import Company, Business


class CompanyQuery(graphene.ObjectType):
    companies = graphene.List(CompanyType)
    company = graphene.Field(CompanyType, id=graphene.Int())

    def resolve_companies(self, info):
        return Company.objects.all()

    def resolve_company(self, info, id):
        if Company.objects.filter(id=id).exists():
            return Company.objects.get(id=id)

        return None


class BusinessQuery(graphene.ObjectType):
    businesses = graphene.List(BusinessType)
    business = graphene.Field(BusinessType, id=graphene.Int())

    def resolve_businesses(self, info):
        return Business.objects.all()

    def resolve_business(self, info, id):
        if Business.objects.filter(id=id).exists():
            return Business.objects.get(id=id)

        return None
