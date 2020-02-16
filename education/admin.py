from django.contrib import admin
from .models import Education


class EducationAdmin(admin.ModelAdmin):
    list_display = ('user', 'school', 'qualification')
    list_filter = ('school', 'qualification')

admin.site.register(Education, EducationAdmin)
