# Generated by Django 3.2.7 on 2021-09-16 20:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0007_alter_chatroom_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroom',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
