# Generated by Django 2.2.7 on 2019-12-16 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0013_auto_20191215_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='guild',
            name='guildContactId',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='guild',
            name='guildContactName',
            field=models.CharField(default='guild_contact', max_length=32),
        ),
    ]
