# Generated by Django 4.1.6 on 2024-05-29 09:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0005_alter_newsletter_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 29, 9, 15, 10, 814223, tzinfo=datetime.timezone.utc)),
        ),
    ]