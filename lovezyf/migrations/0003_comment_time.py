# Generated by Django 3.0.2 on 2020-02-13 17:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lovezyf', '0002_remove_comment_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 14, 1, 11, 36, 868362)),
        ),
    ]