from django.db import models
from random import choice


class PostManager(models.Manager):
    def tag_posts(self, tag):
        return self.filter(tags__name__in=[tag])
    
    def author_posts(self, username):
        return self.filter(Q(author__username=username))

    def recent_posts(self, post):
        tag = choice(post.tags.all())
        return self.filter(tags__name__in=[tag])[:3]