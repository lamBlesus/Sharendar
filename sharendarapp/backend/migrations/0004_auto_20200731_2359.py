# Generated by Django 2.2 on 2020-07-31 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20200731_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='description',
            field=models.CharField(max_length=300),
        ),
    ]