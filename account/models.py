from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from .states import STATE_CHOICES, STATUS_CHOICES


class User(AbstractUser):
    """
    Custom User Model
    """
    phone           = models.CharField(max_length=35, unique=True)
    email           = models.EmailField(unique=True)
    lekki           = models.BooleanField(default=False)
    ikoyi           = models.BooleanField(default=False)
    eko_atlantic    = models.BooleanField(default=False)
    is_employer     = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class UserProfile(models.Model):

    ''' User Profile Model '''

    user                    = models.OneToOneField(User, on_delete=models.CASCADE)
    skills                  = models.CharField(max_length=1050)
    about_me                = models.TextField()
    location                = models.CharField(max_length=35, choices=STATE_CHOICES)
    profile_image           = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    background_image        = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    linkedin                = models.URLField(blank=True, null=True)
    facebook                = models.URLField(blank=True, null=True)
    youtube                 = models.URLField(blank=True, null=True)
    github                  = models.URLField(blank=True, null=True)
    twitter                 = models.URLField(blank=True, null=True)
    instagram               = models.URLField(blank=True, null=True)
    publish                 = models.BooleanField(default=False)
    website                 = models.URLField(blank=True, null=True)
    publish_job             = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username}'

    
    def skills_as_list(self):
        # Split Skills with comma
        return self.skills.split(',')
