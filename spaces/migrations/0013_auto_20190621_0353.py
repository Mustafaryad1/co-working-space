# Generated by Django 2.0 on 2019-06-21 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spaces', '0012_auto_20190621_0348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrate',
            name='calm',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1),
        ),
        migrations.AlterField(
            model_name='userrate',
            name='clean',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1),
        ),
        migrations.AlterField(
            model_name='userrate',
            name='internet',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1),
        ),
        migrations.AlterField(
            model_name='userrate',
            name='location',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1),
        ),
        migrations.AlterField(
            model_name='userrate',
            name='staff',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1),
        ),
    ]
