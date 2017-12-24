from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    put_date =models.DateTimeField('date published')
class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choic_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
class member(models.Model):
    UserID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    pwd = models.CharField(max_length=30)
    phone = models.IntegerField()
