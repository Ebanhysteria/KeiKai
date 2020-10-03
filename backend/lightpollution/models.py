from django.db import models
from mongoengine import Document
from mongoengine.fields import (
    StringField,
    ObjectIdField,
)

# Create your models here.

class LightPollution(Document):

    meta = {"collection": "lightpollution"}

    ID = ObjectIdField()
    prueba = StringField()
