# Generated by Django 2.2 on 2020-08-05 19:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0011_auto_20200805_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 5, 19, 0, 17, 868214, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='events',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 5, 19, 0, 17, 868185, tzinfo=utc)),
        ),
    ]
