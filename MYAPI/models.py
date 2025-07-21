from django.db import models

# Create your models here.
class to_do (models.Model):
    title = models.CharField(max_lenght = 40)