# Generated by Django 3.0 on 2020-01-20 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20200120_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='eko_atlantic',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='ikoy',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='lekki',
            field=models.BooleanField(default=False),
        ),
    ]
