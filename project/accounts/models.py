from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
from django.db.models.signals import post_save



class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), related_name='profile', on_delete=models.CASCADE)
    image = models.ImageField(default='profiles/default.png', upload_to='profiles/', verbose_name='Profile Picture')
    bio = models.TextField(max_length=500, verbose_name='Tell us about yourself', blank=True, null=True)
    is_organisor = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.user.username}\'s profile'
    


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_profile, sender=get_user_model())

def update_profile(sender, instance, created, **kwargs):
    instance.profile.save()

post_save.connect(update_profile, sender=get_user_model())

# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)

#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)

#     objects = UserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDs = ['first_name','last_name']

#     class Meta:
#         verbose_name = 'User'
#         verbose_name_plural = 'Users'

#     def __str__(self):
#         return f'{self.user.first_name} {self.user.last_name}'


