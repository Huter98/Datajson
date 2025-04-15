from django.db import models

# Create your models here.

class Userr(models.Model):
    user= models.CharField(max_length=200)
    create= models.DateField(auto_now_add=True)
    permiso= models.BinaryField()

