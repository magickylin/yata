# Generated by Django 2.0.5 on 2019-10-29 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='APIKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tId', models.IntegerField(default=0)),
                ('tName', models.CharField(blank=True, max_length=200)),
                ('key', models.CharField(blank=True, max_length=200)),
                ('lastCheckTS', models.IntegerField(default=0)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]