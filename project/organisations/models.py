from django.db import models
from django.db.models.signals import pre_save
from Settings.behaviors import Addressable, Slugable, Timingable, Descriptionable
from django.utils.text import slugify
from django.contrib.auth import get_user_model

User = get_user_model()

class OrganisationManager(models.Manager):
    def pending_oragnisations(self):
        return self.filter(is_pending=True)

    def approved_oragnisations(self):
        return self.filter(is_approved=True)

    def rejected_oragnisations(self):
        return self.filter(is_rejected=True)

class Organisation(Addressable, Slugable, Timingable, Descriptionable, models.Model):
    organisor = models.OneToOneField(User, related_name='organisation', on_delete=models.CASCADE, db_constraint=False)
    name = models.CharField(max_length=50)
    image = models.ImageField(blank=True, null=True, upload_to='organisations/')
    is_approved = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    is_pending = models.BooleanField(default=True)

    objects = OrganisationManager()

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     from django.core.urlresolvers import reverse
    #     return reverse('', kwargs={'pk': self.pk})


def set_organisation_slug(sender,instance,*args, **kwargs):
    instance.slug = slugify(instance.name)

pre_save.connect(set_organisation_slug, sender=Organisation)