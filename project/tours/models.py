from django.db import models
from Settings.behaviors import (Slugable, Titleable, Priceable, Descriptionable, Contentable) 

class Tour(Titleable, Priceable, Descriptionable, Contentable,Slugable,models.Model):

    days = models.IntegerField(default=1)
    nights = models.IntegerField(default=0)

    def __str__(self):
        return self.title
