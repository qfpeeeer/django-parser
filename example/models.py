from django.db import models


# Create your models here.

class Data(models.Model):
    title = models.CharField(max_length=150)
    link = models.URLField(max_length=150)
    price = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title