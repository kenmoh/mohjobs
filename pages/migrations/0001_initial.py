# Generated by Django 3.0.2 on 2020-02-05 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=125)),
                ('message', models.TextField()),
            ],
        ),
    ]
