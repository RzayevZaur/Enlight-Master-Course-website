# Generated by Django 4.2.6 on 2023-11-23 18:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_events_models_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='events_models',
            name='location_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]