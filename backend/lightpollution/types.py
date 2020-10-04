from graphene_mongo import MongoengineObjectType
from graphene.relay import Node
from .models import LightPollution

class LightPollutionType(MongoengineObjectType):
    
    class Meta:
        model = LightPollution
        interfaces = (Node, )