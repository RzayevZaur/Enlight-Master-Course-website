# Generated by Django 4.2.6 on 2023-11-26 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_events_video_models'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events_video_models',
            old_name='img',
            new_name='video',
        ),
    ]
