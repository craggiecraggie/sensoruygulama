from __future__ import unicode_literals

from django.db import models

from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class Scklk(models.Model):
    veris = models.CharField(max_length=80)
    verin = models.CharField(max_length=80)
       
class Hrkt(models.Model):
    verih = models.CharField(max_length=80)
