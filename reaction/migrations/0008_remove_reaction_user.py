# Generated by Django 3.0.5 on 2020-05-20 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reaction', '0007_reaction_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reaction',
            name='user',
        ),
    ]
