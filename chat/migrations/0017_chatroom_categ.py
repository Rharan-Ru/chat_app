# Generated by Django 3.2.7 on 2021-10-17 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0016_remove_chatroom_categ'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroom',
            name='categ',
            field=models.ManyToManyField(blank=True, null=True, to='chat.Categorias'),
        ),
    ]
