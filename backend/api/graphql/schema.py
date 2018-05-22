import graphene

from api.graphql.mutations.user import ChangeUserMutation
from api.graphql.queries.user import UserQuery
from api.graphql.queries.accounts import (EmployeeQuery, EmployerQuery)
from api.graphql.queries.jobs import CompanyQuery, BusinessQuery


class Mutation(graphene.ObjectType):
    changeUser = ChangeUserMutation.Field()


class Query(UserQuery, EmployeeQuery, EmployerQuery,
            CompanyQuery, BusinessQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
