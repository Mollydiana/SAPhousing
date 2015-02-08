from django.db import models
from geoposition.fields import GeopositionField

# Create your models here.

import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    LANDLORD = 0
    TENANT = 1
    TYPE = (
        (LANDLORD, "landlord"),
        (TENANT, "tenant")
    )
    user_type = models.IntegerField(choices=TYPE, default=0)

    def __unicode__(self):
        return self.username


class Rental(models.Model):
    title = models.CharField(max_length=100)
    status = models.BooleanField(default=True) # true yes its avaliable
    position = GeopositionField()
    owner = models.ForeignKey(Account,related_name='rentals')
    pricing = models.DecimalField(max_digits=6, decimal_places=2)
    default_picture = models.ForeignKey("Picture", related_name="rentals", blank=True, null=True)

class Picture(models.Model):
    image = models.ImageField(upload_to='media/product_pictures', blank=True, null=True)
    description = models.CharField(max_length=140, blank=True, null=True)
    # default_picture = models.BooleanField(default=False)
    rental = models.ForeignKey(Rental, related_name='pictures')

    def __unicode__(self):
        return 'img{}-{}'.format(self.id, self.rental.title)