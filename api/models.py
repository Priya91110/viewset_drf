from rest_framework import serializers
from django.db import models

# Create your models here.


class Car(models.Model):
    company_name = models.CharField(max_length=100)
    country_name = models.CharField(max_length=100)
    price = models.IntegerField()
    mileage = models.IntegerField()
    fuel_type = models.CharField(max_length=100)


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"