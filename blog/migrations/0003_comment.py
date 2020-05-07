# Generated by Django 3.0.5 on 2020-05-01 21:28

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_like'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=150)),
                ('body', models.TextField()),
                ('added_date', models.DateTimeField(default=datetime.datetime(2020, 5, 1, 21, 28, 17, 478048, tzinfo=utc))),
                ('approved_comment', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_comments', to='blog.Post')),
            ],
            options={
                'verbose_name_plural': 'Documentation of Comments',
            },
        ),
    ]
