# Generated by Django 2.2 on 2020-06-13 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0003_auto_20200607_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendorprofile',
            name='total_compact',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vendorprofile',
            name='total_sedan',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vendorprofile',
            name='total_suv',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]