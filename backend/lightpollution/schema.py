import graphene
from graphene.relay import Node
from graphene_mongo.fields import MongoengineConnectionField
from .models import LightPollution
from .types import LightPollutionType
from .mutations import CreateLightPollutionMutation

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
