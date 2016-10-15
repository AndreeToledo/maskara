from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Mask(models.Model):
    origin_number = models.CharField(max_length=30)
    mask_number = models.CharField(max_length=30)
    target_number = models.CharField(max_length=30)
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)
