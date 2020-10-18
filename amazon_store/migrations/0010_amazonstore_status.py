# Generated by Django 3.0.5 on 2020-10-17 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazon_store', '0009_auto_20201017_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='amazonstore',
            name='status',
            field=models.CharField(choices=[('N', 'New'), ('R', 'Recent')], default='N', max_length=10),
        ),
    ]