# Generated by Django 4.2.1 on 2023-09-03 13:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.FileField(upload_to='profile_photos')),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pin_name', models.CharField(max_length=200)),
                ('Pin_img', models.FileField(upload_to='PINS')),
                ('Pin_discription', models.TextField()),
                ('Pin_time', models.DateTimeField(auto_now_add=True)),
                ('Likes', models.ManyToManyField(blank=True, null=True, related_name='likes', to=settings.AUTH_USER_MODEL)),
                ('Pin_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Comment', models.TextField(blank=True, null=True)),
                ('Comment_timming', models.DateTimeField(auto_now_add=True)),
                ('Comment_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Comment_on', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pinapp.pin')),
            ],
        ),
    ]
