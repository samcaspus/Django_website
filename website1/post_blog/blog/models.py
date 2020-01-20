from django.db import models

# Create your models here.
class blogging(models.Model):
    user = models.CharField(max_length=100)
    data = models.TextField()
    publish = models.BooleanField(default = False)
    