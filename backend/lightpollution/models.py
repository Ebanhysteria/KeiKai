from django.db import models
from mongoengine import Document
from mongoengine.fields import (
    StringField,
    IntField,
    FloatField,
    ListField,
    ObjectIdField,
    BooleanField,
)

# Create your models here.

class LightPollution(Document):

    meta = {"collection": "lightpollution"}

    ID = ObjectIdField()
    sourceposition = ListField()
    targetPosition = ListField()
    longitude = FloatField()
    latitude = FloatField()


class Species(Document):

    meta = {"collection": "species"}

    ID = ObjectIdField()
    year = IntField()
    occurrenceStatus = StringField()
    scientificName = StringField()
    basisOfRecord = StringField()
    coordinateUncertaintyInMeters = IntField()
    hasCoordinate = BooleanField()
    hasGeospatialIssue = BooleanField()
