# Generated by Django 4.1.6 on 2024-06-03 04:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0006_alter_newsletter_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 3, 4, 31, 19, 100815, tzinfo=datetime.timezone.utc)),
        ),
    ]
