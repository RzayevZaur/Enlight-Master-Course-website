# Generated by Django 4.2.6 on 2023-11-26 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_about_video_models_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='index_models',
            old_name='first_name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='index_models',
            name='instrument',
        ),
        migrations.RemoveField(
            model_name='index_models',
            name='last_name',
        ),
        migrations.AddField(
            model_name='index_models',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='img', verbose_name='index img'),
        ),
    ]