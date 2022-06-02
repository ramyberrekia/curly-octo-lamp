from django.db import models
from django.shortcuts import reverse
from Settings.behaviors import (Slugable, Titleable, Priceable,Placeable, Descriptionable, Contentable, Addressable, Timingable) 
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.db.models import Q

class HotelManager(models.Manager):
    def related_hotels(self, place):
        return self.filter(place=place)

    def filter_by_place(self, place):
        return self.filter(Q(place__name__icontains=place))

class Hotel(Titleable, Priceable, Placeable,Descriptionable, Contentable, Addressable,Slugable,Timingable,models.Model):
    display_image = models.ImageField(upload_to='hotels/', verbose_name='Image')

    objects = HotelManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('hotels:hotels_detail', kwargs={'slug':self.slug})

class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, related_name='images', on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='hotels/', verbose_name='Image')


def set_hotel_slug(sender,instance,*args, **kwargs):
    instance.slug = slugify(instance.title)

pre_save.connect(set_hotel_slug, sender=Hotel)


