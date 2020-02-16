from django.contrib import admin
from .models import Experience


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('user', 'company_name', 'job_title', 'job_description')
    list_filter = ('company_name', 'job_title')

admin.site.register(Experience, ExperienceAdmin)
