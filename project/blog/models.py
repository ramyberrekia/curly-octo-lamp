from django.db import models
from django.contrib.auth import get_user_model
from Settings.behaviors import Authorable, Slugable, Timingable
from taggit.managers import TaggableManager
from django.db.models import Q
from django.db.models.signals import pre_save
from django.utils.text import slugify

class PostManager(models.Manager):
    def tag_posts(self, tag):
        return Post.objects.filter(tags__name__in=[tag])
    
    def author_posts(self, username):
        return Post.objects.filter(Q(author__username=username))


class Post(Authorable, Slugable, Timingable, models.Model):
    title = models.CharField(max_length=25)
    tags = TaggableManager()
    content = models.TextField(max_length=1999999)
    display_pic = models.ImageField(upload_to='post/', verbose_name='picture')
    objects = PostManager()

    def __str__(self):
        return self.title

def slug_title(sender, instance, *args, **kwargs):
    print(instance.slug)
    instance.slug = slugify(instance.title)

pre_save.connect(slug_title, sender=Post)
