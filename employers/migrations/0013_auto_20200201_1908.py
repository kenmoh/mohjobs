# Generated by Django 3.0.2 on 2020-02-01 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employers', '0012_delete_companyprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='deleted_after_30_days',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='jobpost',
            name='deleted_after_45_days',
            field=models.BooleanField(default=False),
        ),
    ]
