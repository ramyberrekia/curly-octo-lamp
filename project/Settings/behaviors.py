from django.db import models
from django.contrib.auth import get_user_model
from places.models import Place

class Authorable(models.Model):
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    class Meta:
        abstract = True
         
class Slugable(models.Model):
    slug = models.SlugField(blank=True, null=True)

    class Meta:
        abstract = True

class Titleable(models.Model):
    title = models.CharField(max_length=25, unique=True, primary_key=True)

    class Meta:
        abstract = True

class Priceable(models.Model):
    price = models.IntegerField(default=0)

    class Meta:
        abstract = True

class Descriptionable(models.Model):
    description = models.TextField(max_length=150)

    class Meta:
        abstract = True

class Contentable(models.Model):
    content = models.TextField(max_length=11577000)

    class Meta:
        abstract = True

class Placeable(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Addressable(models.Model):
    address = models.CharField(max_length=100)

    class Meta:
        abstract = True

class Timingable(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

