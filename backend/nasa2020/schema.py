import graphene

from lightpollution.schema import LightPollutionMutations, LightPollutionQuery


class Query(LightPollutionQuery, graphene.ObjectType):
    pass


class Mutations(LightPollutionMutations, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutations)