# Generated by Django 3.2.7 on 2021-10-17 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0012_auto_20211017_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroom',
            name='categ',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.categorias'),
        ),
    ]