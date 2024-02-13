# Generated by Django 4.2.6 on 2023-11-26 07:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_events_models_location_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='events_models',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]