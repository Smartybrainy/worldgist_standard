# Generated by Django 3.0.5 on 2020-07-08 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0007_video_url_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_file',
            field=models.FileField(blank=True, null=True, upload_to='videos/%y/%m/%d/'),
        ),
    ]
