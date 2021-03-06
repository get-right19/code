from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Topic(models.Model):
    top_name =models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic=models.ForeignKey
    name =models.CharField(max_length=264,unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name= models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date= models.DateField()

    def __str__(self):
        return str(self.date)

