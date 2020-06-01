from django.db import models
from django.contrib.auth.models import User
import datetime as dt
# from tinymce.models import HTMLField

# Create your models here.


class Profile(models.Model):
    title = models.CharField(max_length =30)
    Bio = models.TextField(max_length = 150, blank=True)

    def __str__(self):
        return self.title

    def save_profile(self):
        self.save()

