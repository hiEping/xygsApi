# Generated by Django 3.2.9 on 2021-12-03 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0004_auto_20211129_0502'),
    ]

    operations = [
        migrations.AddField(
            model_name='poi',
            name='port',
            field=models.IntegerField(default=80),
        ),
    ]
