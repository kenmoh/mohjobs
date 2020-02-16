from django.conf import settings
from django.db import models
from account.models import User

 
class Experience(models.Model):
   
    ''' Experience '''

    user                    = models.ForeignKey(User, on_delete = models.CASCADE, blank=True, null=True)
    company_name            = models.CharField(max_length=255)
    job_title               = models.CharField(max_length=255)
    year_from               = models.IntegerField()
    year_to                 = models.IntegerField()
    job_description         = models.TextField()

    def __str__(self):
        return f'{self.user}'



