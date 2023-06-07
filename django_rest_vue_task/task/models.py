from django.db import models


# Create your models here.

class Person(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=300)

    def __str__(self):
        return self.email
