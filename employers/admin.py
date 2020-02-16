from django.contrib import admin
from .models import JobPost


class JobPostAdmin(admin.ModelAdmin):
    list_display = ('user', 'job_title', 'job_requirement', 'years_experience', 'job_location', 'publish')
    list_filter = ('job_title', 'years_experience', 'job_location', 'publish')


admin.site.register(JobPost, JobPostAdmin)

