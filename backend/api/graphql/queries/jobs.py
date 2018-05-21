import graphene

from api.graphql.types.jobs import CompanyType
from jobs.models import Company


class CompanyQuery(graphene.ObjectType):
    companies = graphene.List(CompanyType)
    company = graphene.Field(CompanyType, id=graphene.Int())

    def resolve_companies(self, info):
        return Company.objects.all()

    def resolve_company(self, info, id):
        if Company.objects.filter(id=id).exists():
            return Company.objects.get(id=id)

        return None
