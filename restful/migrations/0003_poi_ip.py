# Generated by Django 3.2.9 on 2021-11-29 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0002_auto_20211129_0342'),
    ]

    operations = [
        migrations.AddField(
            model_name='poi',
            name='ip',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
    ]