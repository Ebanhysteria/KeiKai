from graphene_mongo import MongoengineObjectType
from graphene.relay import Node
from .models import LightPollution, Species

class LightPollutionType(MongoengineObjectType):
    
    class Meta:
        model = LightPollution
        interfaces = (Node, )

class SpeciesType(MongoengineObjectType):

    class Meta:
        model = Species
        interfaces = (Node, )