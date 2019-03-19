from django.db import models
from datetime import datetime
from django.utils import dateformat
from django import forms
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.
class UserProfileInfo(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE)
  portfolio_site = models.URLField(blank=True)
  birth_date= models.DateField('Birthday (mm/dd/yy)')
def __str__(self):
    return self.user.username