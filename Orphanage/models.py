from django.db import models

# Create your models here.
class Children(models.Model):
    first_name = models.CharField(max_length=30)
    sur_name = models.CharField(max_length=30)
    age       = models.IntegerField()
    religon   = models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.first_name} {self.sur_name}"

class Admin(models.Model):
    children    = models.ForeignKey(Children, on_delete=models.CASCADE)
    name        = models.CharField(max_length=30) 
    contact     = models.IntegerField()

class Adoption(models.Model):
    children        = models.ForeignKey(Children, on_delete=models.CASCADE)
    first_name      = models.CharField(max_length=30)
    sur_name        = models.CharField(max_length=30)
    date_of_birth   = models.DateField()
    address         = models.TextField()
    phone_number    = models.CharField(max_length=11)

    def __str__(self):
        return f"{self.first_name} {self.sur_name}"


class StatusForChildren(models.Model):
    children        = models.ForeignKey(Children, on_delete=models.CASCADE)
    adoption        = models.OneToOneField(Adoption, on_delete=models.CASCADE)
    STATUS_CHOICE  = (
        ('A', 'Approved'),
        ('D', 'Denied'),
        ('P', 'Pending')
    ) 
    status  = models.CharField(max_length=30    , choices = STATUS_CHOICE )
