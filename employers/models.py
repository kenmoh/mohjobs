from django.db import models
from datetime import datetime
from account.models import User
from account.states import STATE_CHOICES, JOB_STATUS


# class CompanyProfile(models.Model):
#     """ Employer Model """
#     user                = models.OneToOneField(User, on_delete=models.CASCADE)
#     location            = models.CharField(max_length=100, choices=STATE_CHOICES)
#     website             = models.URLField(blank=True, null=True)
#     profile_image       = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
#     background_image    = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
#     publish             = models.BooleanField(default=False)

#     def __str__(self):
#         return f'{self.user.username}'

class JobPost(models.Model):
    """ Post Job Model """
    user                    = models.ForeignKey(User, on_delete=models.CASCADE)
    job_title               = models.CharField(max_length=100)
    job_requirement         = models.CharField(max_length=1050)
    years_experience        = models.IntegerField()
    job_description         = models.TextField()
    job_location            = models.CharField(max_length=35, choices=STATE_CHOICES)
    application_link        = models.URLField(blank=True, null=True)
    application_email       = models.EmailField(null=True, blank=True)
    publish                 = models.BooleanField(default=False)
    date_posted             = models.DateField(auto_now_add=True)
    deleted_after_30_days   = models.BooleanField(default=False)
    deleted_after_45_days   = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username}'

    def job_requirements_as_list(self):
        # Split Skills with comma
        return self.job_requirement.split(',')

    