import graphene
from graphql import GraphQLError
from django.core.exceptions import ObjectDoesNotExist

from .models import LightPollution, Species
from .types import LightPollutionType, SpeciesType
#from .integration import GBIF

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

class SpeciesInput(graphene.InputObjectType):
    id = graphene.ID()
    year = graphene.Int()
    occurrenceStatus = graphene.String()
    scientificName = graphene.String()
    basisOfRecord = graphene.String()
    coordinateUncertaintyInMeters = graphene.Int()
    hasCoordinate = graphene.Boolean()
    hasGeospatialIssue = graphene.Boolean()

class CreateSpeciesMutation(graphene.Mutation):

    species = graphene.Field(SpeciesType)

    class Arguments:
        species_data = SpeciesInput(required=True)

    def mutate(self, info, species_data=None):

        species = Species(
            year = species_data.year,
            occurrenceStatus = species_data.occurrenceStatus,
            scientificName = species_data.scientificName,
            basisOfRecord = species_data.basisOfRecord,
            coordinateUncertaintyInMeters = species_data.coordinateUncertaintyInMeters,
            hasCoordinate = species_data.hasCoordinate,
            hasGeospatialIssue = species_data.hasGeospatialIssue,
        )

        species.save()

        return CreateSpeciesMutation(
            species=species
        )