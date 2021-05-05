from django.db import models

# Create your models here.
class Wishlist(models.Model):
  name = models.CharField(max_length=64)