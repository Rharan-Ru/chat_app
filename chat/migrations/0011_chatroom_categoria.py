# Generated by Django 3.2.7 on 2021-10-17 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0010_alter_chatroom_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroom',
            name='categoria',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
