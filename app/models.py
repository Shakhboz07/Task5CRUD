
from django.db.models import Model, CharField, ImageField


# Create your models here.


class Candidate(Model):
    image = ImageField()
    name = CharField(max_length=255)
    field = CharField(max_length=255)
    address = CharField(max_length=255)


def __str__(self):
    return self.name
