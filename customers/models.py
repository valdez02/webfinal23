from django.db import models

class Customer(models.Model) :
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
# Create your models here.
