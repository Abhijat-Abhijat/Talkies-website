from django.db import models

# Create your models here.

class feedbackModel(models.Model):
    name = models.CharField(max_length=35)
    email = models.EmailField()
    contact = models.BigIntegerField()
    message = models.TextField()
    