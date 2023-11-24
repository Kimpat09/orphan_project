from django.db import models

# Create your models here.

class Children(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age       = models.IntegerField(max_length=30)
    gender    = models.CharField(max_length=30)

class Adoption_form(models.Model):
    first_name      = models.CharField(max_length=30)
    age             = models.IntegerField(max_length=30)
    date_of_birth   = models.IntegerField(max_length=30)
    place_of_birth  = models.CharField(max_length=30)
    nationality     = models.CharField(max_length=30)
    religon         = models.CharField(max_length=30)
    address         = models.TextField(max_length=30)
    phone_number    = models.IntegerField(max_length=30)
    
