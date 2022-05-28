from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=25)
    image = models.ImageField(upload_to='places/')

    def __str__(self):
        return self.name