# Generated by Django 2.0 on 2019-06-21 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spaces', '0016_auto_20190621_0401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='photo',
            field=models.ImageField(upload_to='room/photos/'),
        ),
    ]
