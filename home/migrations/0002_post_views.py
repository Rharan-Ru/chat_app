# Generated by Django 3.2.7 on 2021-09-18 22:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.ManyToManyField(related_name='views', to=settings.AUTH_USER_MODEL),
        ),
    ]
