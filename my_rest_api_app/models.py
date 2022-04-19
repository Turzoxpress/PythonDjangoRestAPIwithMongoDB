from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.TextField(max_length=200)
    def __str__(self):
        return self.name