# Generated by Django 2.0 on 2019-06-21 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spaces', '0014_auto_20190621_0357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrate',
            name='calm',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='userrate',
            name='clean',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='userrate',
            name='internet',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='userrate',
            name='location',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='userrate',
            name='staff',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2),
        ),
    ]
