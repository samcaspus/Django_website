from django.db import models

# Create your models here.

class he_qa_calendar(models.Model):
    name = models.CharField(max_length = 150)
    day = models.IntegerField()
    month = models.IntegerField()
    