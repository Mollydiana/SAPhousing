from django.db import models
from geoposition.fields import GeopositionField

# Create your models here.

import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


class People(AbstractUser):
    LANDLORD = 0
    TENANT = 1
    TYPE = (
        (LANDLORD, "landlord"),
        (TENANT, "tenant")
    )
    user_type = models.PositiveSmallIntegerField(choices=TYPE, default=0)
    name = models.CharField(max_length=100, blank=True, null=True)

class Issue(models.Model):
    date = models.DateField(default=datetime.date.today())
    user = models.ForeignKey(People, related_name='issues')
    type = models.TextField(max_length=50, blank=True, null=True)
    status_issue = models.IntegerField(default=0)
    position = GeopositionField()
