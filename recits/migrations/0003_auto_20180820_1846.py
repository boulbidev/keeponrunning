# Generated by Django 2.0.8 on 2018-08-20 16:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('recits', '0002_recitpage_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recitpage',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Date de création du récit'),
        ),
    ]
