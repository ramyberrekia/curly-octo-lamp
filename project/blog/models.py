from django.db import models
from django.contrib.auth import get_user_model
from Settings.behaviors import Authorable, Slugable, Timingable
from taggit.managers import TaggableManager
from django.db.models import Q
from django.db.models.signals import pre_save
from django.utils.text import slugify
from PIL import Image
from sorl.thumbnail import get_thumbnail
from .managers import PostManager
from django.shortcuts import reverse


class PostQuerySet(models.QuerySet):
    def get_post_tags(self, post):
        return post.tags.all()
        


class Post(Authorable, Slugable, Timingable, models.Model):
    title = models.CharField(max_length=25)
    tags = TaggableManager()
    content = models.TextField(max_length=1999999)
    display_pic = models.ImageField(upload_to='post/', verbose_name='picture')
    objects = PostManager()
    # objects = PostQuerySet.as_manager()

    def __str__(self):
        return self.title

    def get_img_url(self):
        return self.display_pic.url

    def get_absolute_url(self):
        return reverse('blog:posts_detail', kwargs={'slug':self.slug})

def pre_save_settings(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title)
    # instance.display_pic = get_thumbnail(instance.display_pic,'250x250', quality=99,format=Image.open(instance.display_pic).format).url
    img = Image.open(instance.display_pic)
    if img.width != 853 or img.height != 894 :
        output = (894,853)
        img.thumbnail(output) 
        img.save(instance.display_pic.path)


pre_save.connect(pre_save_settings, sender=Post)
