# Generated by Django 2.0 on 2019-03-26 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spaces', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userrate',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]