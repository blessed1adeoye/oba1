# Generated by Django 3.2 on 2022-06-13 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('b', '0008_testimony_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='res',
            name='url',
            field=models.URLField(blank=True, default=None),
        ),
    ]
