from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    date_of_birth = models.DateField()
    country_of_origin = models.CharField(max_length=50)