# Generated by Django 3.0.6 on 2021-08-25 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210824_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='banner_image',
            field=models.ImageField(upload_to='public/static/blog'),
        ),
    ]