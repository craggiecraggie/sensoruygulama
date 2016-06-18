from __future__ import unicode_literals

from django.db import models

from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class Scklk(models.Model):
    ver1 = models.CharField(max_length=80)
    ver2 = models.CharField(max_length=80)
       
class Hrkt(models.Model):
    ver3 = models.CharField(max_length=80)
