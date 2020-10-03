import graphene
from graphql import GraphQLError
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime

from .models import LightPollution
from .types import LightPollutionType

class LightPollutionInput(graphene.InputObjectType):
    id = graphene.ID()
    longitude = graphene.Float()
    latitude = graphene.Float()
    sourceposition = graphene.List(graphene.Float)
    targetPosition = graphene.List(graphene.Float)

class CreateLightPollutionMutation(graphene.Mutation):

    light_pollution = graphene.Field(LightPollutionType)

    class Arguments:
        light_pollution_data = LightPollutionInput(required=True)

    def mutate(self, info, light_pollution_data=None):

        light_pollution = LightPollution(
            longitude = light_pollution_data.longitude,
            latitude = light_pollution_data.latitude,
            sourceposition = light_pollution_data.sourceposition,
            targetPosition = light_pollution_data.targetPosition,
        )

        light_pollution.save()

        return CreateLightPollutionMutation(
            light_pollution=light_pollution
        )