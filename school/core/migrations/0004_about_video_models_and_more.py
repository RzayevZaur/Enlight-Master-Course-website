# Generated by Django 4.2.6 on 2023-11-26 16:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_galery_models_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='about_video_models',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('video', models.FileField(blank=True, null=True, upload_to='video', verbose_name='about video')),
            ],
        ),
        migrations.RenameField(
            model_name='about_models',
            old_name='first_name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='about_models',
            name='instrument',
        ),
        migrations.RemoveField(
            model_name='about_models',
            name='last_name',
        ),
        migrations.AddField(
            model_name='about_models',
            name='Description',
            field=models.TextField(default=django.utils.timezone.now, max_length=10000),
            preserve_default=False,
        ),
    ]
