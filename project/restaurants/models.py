from django.db import models
from Settings.behaviors import (Slugable, Titleable, Priceable, Descriptionable, Contentable, Addressable) 

class Restaurant(Titleable, Priceable, Descriptionable, Contentable, Addressable,Slugable,models.Model):

    def __str__(self):
        return self.title
