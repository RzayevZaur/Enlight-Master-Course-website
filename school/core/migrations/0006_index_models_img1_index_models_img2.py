# Generated by Django 4.2.6 on 2023-12-02 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_first_name_index_models_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='index_models',
            name='img1',
            field=models.ImageField(blank=True, null=True, upload_to='img', verbose_name='index img'),
        ),
        migrations.AddField(
            model_name='index_models',
            name='img2',
            field=models.ImageField(blank=True, null=True, upload_to='img', verbose_name='index img'),
        ),
    ]
