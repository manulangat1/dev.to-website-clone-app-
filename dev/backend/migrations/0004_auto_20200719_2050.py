# Generated by Django 3.0.8 on 2020-07-19 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_like_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='likes',
            field=models.BooleanField(default=False),
        ),
    ]