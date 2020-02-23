from django.db import models

from django.conf import settings
from django.db import models
from django.contrib.sessions.models import Session
from django.contrib.auth.models import AbstractUser
from django.utils import timezone



class Post(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title