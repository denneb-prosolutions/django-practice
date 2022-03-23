from django.db import models
from django.forms import DateTimeField

# Create your models here.
class Acticles(models.Model):
    article_name = models.CharField(max_length=60)
    article_description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.article_name
