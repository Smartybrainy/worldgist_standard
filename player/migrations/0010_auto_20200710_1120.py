# Generated by Django 3.0.5 on 2020-07-10 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0009_video_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='disc',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='desc',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]