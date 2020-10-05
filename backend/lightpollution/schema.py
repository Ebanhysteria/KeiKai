import graphene
from graphene.relay import Node
from graphene_mongo.fields import MongoengineConnectionField
from .models import LightPollution, Species
from .types import LightPollutionType, SpeciesType
from .mutations import CreateLightPollutionMutation, CreateSpeciesMutation

class LightPollutionMutations(graphene.ObjectType):
    create_light_pollution = CreateLightPollutionMutation.Field()

class LightPollutionQuery(graphene.ObjectType):
    light_pollution_ = Node.Field(LightPollutionType)
    light_pollution_list = MongoengineConnectionField(LightPollutionType)
    
    def resolve_light_pollution_list(self, info, **kwargs):
        
        if kwargs:
            return LightPollution.objects.filter(**kwargs)
        else:
            return LightPollution.objects.all()


class SpeciesMutations(graphene.ObjectType):
    create_species = CreateSpeciesMutation.Field()

class SpeciesQuery(graphene.ObjectType):
    species_ = Node.Field(SpeciesType)
    species_list = MongoengineConnectionField(SpeciesType)

    def resolve_species_list(self, info, **kwargs):

        if kwargs:
            return Species.objects.filter(**kwargs)
        else:
            return Species.objects.all()
