from django.db import models

# Create your models here.

class Data(models.Model):
    image_name=models.CharField(max_length=200)
    objects_detected=models.CharField(max_length=200)
    timestamp=models.CharField(max_length=100)