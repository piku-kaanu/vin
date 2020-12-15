from django.db import models


class Vin(models.Model):
    value = models.CharField(max_length=30)
    valueId = models.CharField(max_length=30)
    variable = models.CharField(max_length=30)
    variableId = models.CharField(max_length=30)
