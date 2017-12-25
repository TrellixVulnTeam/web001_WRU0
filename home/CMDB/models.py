from django.db import models

# Create your models here.
class member(models.Model):
    UserID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    pwd = models.CharField(max_length=30)
    phone = models.IntegerField()
