# Generated by Django 3.0 on 2020-01-21 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employers', '0008_auto_20200109_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyprofile',
            name='counter',
            field=models.IntegerField(default=0),
        ),
    ]
