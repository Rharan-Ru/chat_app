# Generated by Django 3.2.7 on 2021-10-17 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0015_auto_20211017_1920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatroom',
            name='categ',
        ),
    ]
