from django.db import models

# Create your models here.


class Apartment(models.Model):
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.name