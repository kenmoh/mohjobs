# Generated by Django 3.0 on 2020-01-07 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employers', '0003_companyprofile_publish'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companyprofile',
            name='company_name',
        ),
    ]
