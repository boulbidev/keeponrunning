# Generated by Django 2.0.8 on 2018-08-28 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0021_image_file_hash'),
        ('recits', '0005_recitpagegalleryimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='recitpage',
            name='hero_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]