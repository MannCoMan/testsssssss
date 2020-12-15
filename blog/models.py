from django.db import models

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name
