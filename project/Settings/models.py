from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class siteSettings(models.Model):
    logo = models.ImageField(upload_to='logo/')
    site_name = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    phone_number = PhoneNumberField()
    description = models.TextField(max_length=150)
    instagram_url = models.URLField()
    facebook_url = models.URLField()
    twitter_url = models.URLField()
    

    class Meta:
        verbose_name_plural = 'Settings' 



