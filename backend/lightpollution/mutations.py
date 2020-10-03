import graphene
from graphql import GraphQLError
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime

from .models import LightPollution
from .types import LightPollutionType

class LightPollutionInput(graphene.InputObjectType):
    id = graphene.ID()
    prueba = graphene.String()

class CreateLightPollutionMutation(graphene.Mutation):

    light_p = graphene.Field(LightPollutionType)

    class Arguments:
        light_p_data = LightPollutionInput(required=True)

    def mutate(self, info, light_p_data=None):

        light_p = LightPollution(
            prueba = light_p_data.prueba,
        )

        light_p.save()

        return CreateLightPollutionMutation(
            light_p = light_p,
        )