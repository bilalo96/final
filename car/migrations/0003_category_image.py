# Generated by Django 4.1.6 on 2023-10-30 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_alter_carreview_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default='default_image.jpg', upload_to='categoryimages/'),
        ),
    ]
