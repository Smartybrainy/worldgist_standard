# Generated by Django 3.0.5 on 2020-09-04 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20200904_0301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(),
        ),
    ]