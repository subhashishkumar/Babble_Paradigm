# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.exceptions import ObjectDoesNotExist


# Create your models here.
class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    unit = models.CharField(max_length=30)

    def __unicode__(self):
        try:
            return '{} {}'.format(self.user, self.unit)
        except ObjectDoesNotExist:
            return "[profile instance]"


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user=instance)
    try:
        instance.profile.save()
    except AttributeError:
        myprofile = profile.objects.create(user=instance)
        myprofile.save()
