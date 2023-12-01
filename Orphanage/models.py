from django.db import models

# Create your models here.
class Children(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age       = models.IntegerField()
    religon   = models.CharField(max_length=30)
    location  = models.CharField(max_length=30)

class Admin(models.Model):
    children    = models.ForeignKey(Children, on_delete=models.CASCADE)
    name        = models.CharField(max_length=30) 
    contact     = models.IntegerField()

class Adoption(models.Model):
    children        = models.ForeignKey(Children, on_delete=models.CASCADE)
    first_name      = models.CharField(max_length=30)
    date_of_birth   = models.IntegerField()
    address         = models.CharField(max_length=30)
    phone_number    = models.IntegerField()


class StatusForChildren(models.Model):
    children        = models.ForeignKey(Children, on_delete=models.CASCADE)
    adoption        = models.OneToOneField(Adoption, on_delete=models.CASCADE)
    STATUS_CHOICE  = (
        ('A', 'Accept'),
        ('D', 'Denied'),
        ('P ', 'Pending')
    ) 
    status  = models.CharField(max_length=30    , choices = STATUS_CHOICE )
