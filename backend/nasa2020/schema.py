import graphene

from lightpollution.schema import LightPollutionMutations, LightPollutionQuery, SpeciesQuery, SpeciesMutations


class Query(LightPollutionQuery, SpeciesQuery, graphene.ObjectType):
    pass


class Mutations(LightPollutionMutations, SpeciesMutations, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutations)