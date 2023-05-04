from django.db import models


class Customer(models.Model):
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    bmi = models.FloatField()
    children = models.IntegerField()
    smoker = models.CharField(max_length=10)
    region = models.CharField(max_length=20)
    predicted_price = models.FloatField(null=True, blank=True)
