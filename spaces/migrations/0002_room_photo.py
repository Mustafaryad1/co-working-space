# Generated by Django 2.0 on 2019-03-23 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spaces', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='photo',
            field=models.FileField(default=1, upload_to='room/photos/'),
            preserve_default=False,
        ),
    ]
