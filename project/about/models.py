from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=15)
    content = models.TextField(max_length=255)

    def __str__(self):
        return self.title
