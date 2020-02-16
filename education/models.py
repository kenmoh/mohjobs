from django.conf import settings
from django.db import models
from account.models import User


class Education(models.Model):

    ''' Education '''

    user                    = models.ForeignKey(User, on_delete = models.CASCADE, blank=True, null=True)
    school                  = models.CharField(max_length=255)
    field_of_study          = models.CharField(max_length=255)
    qualification           = models.CharField(max_length=255)
    year                    = models.IntegerField()

    def __str__(self):
        return f'{self.user}'
