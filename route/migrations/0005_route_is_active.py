# Generated by Django 3.2.5 on 2021-07-04 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0004_auto_20210704_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]