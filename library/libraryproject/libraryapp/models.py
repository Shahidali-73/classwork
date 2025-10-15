from django.db import models

class Library(models.Model):
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=500)
    year = models.PositiveIntegerField()
