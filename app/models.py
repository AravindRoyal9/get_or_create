from modulefinder import Module
from os import access
from django.db import models

# Create your models here.
class topic(models.Model):
    topic_name=models.CharField(max_length=120,primary_key=True)

    def _str_(self):
        return self.topic_name

class webpage(models.Model):
    topic_name=models.ForeignKey(topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=120)
    url=models.URLField()

    def _str_(self):
        return self.name

class access_records(models.Model):
    name=models.ForeignKey(webpage,on_delete=models.CASCADE)
    date=models.DateField()



