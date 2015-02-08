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
    # The address related
    position = GeopositionField()
    number = models.CharField(max_length=30, blank=True)
    street = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zipcode = models.CharField(max_length=5, blank=True)

    # Rental Property related
    owner = models.ForeignKey(Account,related_name='rentals')
    pricing = models.DecimalField(max_digits=6, decimal_places=2)
    title = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

    # Default showing picture
    default_picture = models.ForeignKey("Picture", related_name="rentals", blank=True, null=True)


class Picture(models.Model):
    image = models.ImageField(upload_to='media/product_pictures', blank=True, null=True)
    description = models.CharField(max_length=140, blank=True, null=True)
    # default_picture = models.BooleanField(default=False)
    rental = models.ForeignKey(Rental, related_name='pictures')

    def __unicode__(self):
        return 'img{}-{}'.format(self.id, self.rental.title)