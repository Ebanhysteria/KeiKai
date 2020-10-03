from django.db import models
from mongoengine import Document
from mongoengine.fields import (
    StringField,
    FloatField,
    ListField,
    ObjectIdField,
)

# Create your models here.

class LightPollution(Document):

    meta = {"collection": "lightpollution"}

    ID = ObjectIdField()
    sourceposition = ListField()
    targetPosition = ListField()
    longitude = FloatField()
    latitude = FloatField()