# Generated by Django 2.0.5 on 2019-09-30 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0018_auto_20190726_0931'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='player',
            name='validKey',
            field=models.BooleanField(default=True),
        ),
    ]
