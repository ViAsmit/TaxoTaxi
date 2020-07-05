# Generated by Django 2.2 on 2020-05-09 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20200430_1542'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customerprofile',
            old_name='aadharcard_front',
            new_name='document',
        ),
        migrations.RemoveField(
            model_name='customerprofile',
            name='aadharcard_rear',
        ),
        migrations.RemoveField(
            model_name='customerprofile',
            name='driving_licence_front',
        ),
        migrations.RemoveField(
            model_name='customerprofile',
            name='driving_licence_rear',
        ),
        migrations.RemoveField(
            model_name='customerprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='customerprofile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='customerprofile',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='customerprofile',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='customerprofile',
            name='pancard',
        ),
        migrations.RemoveField(
            model_name='customerprofile',
            name='votercard',
        ),
        migrations.AlterField(
            model_name='customerprofile',
            name='address',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
