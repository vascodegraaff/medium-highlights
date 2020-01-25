from django.db import models
from django.conf import settings
import uuid
from model_utils import Choices

# Create your models here.

class Tag(models.Model):
    category = models.CharField(unique=True, max_length=40)
    def __str__(self):
        return self.category

class Article(models.Model):
    title = models.CharField(max_length=120)
    tag = models.CharField(max_length=40)
    url = models.URLField(unique=False)
    claps = models.IntegerField()
    clapStr = models.CharField(max_length=30)
    authur = models.CharField(max_length=40)
    publication = models.CharField(max_length=40)
    date = models.DateField()


    def __str__(self):
        return self.title
    class Meta():
        ordering = ['-claps']

