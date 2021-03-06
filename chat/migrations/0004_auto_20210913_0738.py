# Generated by Django 3.2.7 on 2021-09-13 10:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('chat', '0003_auto_20210912_0834'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to='auth.user')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('image', models.ImageField(blank=True, default='img_profile/default.jpg', upload_to='img_profile/')),
            ],
        ),
        migrations.AlterField(
            model_name='chatroom',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
