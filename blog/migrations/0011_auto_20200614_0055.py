# Generated by Django 3.0.5 on 2020-06-13 23:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200521_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 6, 13, 23, 55, 50, 628790, tzinfo=utc)),
        ),
    ]
