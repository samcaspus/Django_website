from django.db import models

# Create your models here.

class Article(models.Model):
    name = models.CharField(max_length=100)
    data = models.TextField()

    def __str__(self):
        return self.name+"__"+str(self.id)

