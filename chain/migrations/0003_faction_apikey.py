# Generated by Django 2.0.5 on 2018-09-11 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chain', '0002_auto_20180910_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='faction',
            name='apiKey',
            field=models.CharField(default='0', max_length=16),
        ),
    ]