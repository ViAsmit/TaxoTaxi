# Generated by Django 2.2 on 2020-06-20 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0007_auto_20200620_0241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='aadharcard_front',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='driver',
            name='aadharcard_rear',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='driver',
            name='driving_licence_front',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='driver',
            name='driving_licence_rear',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='driver',
            name='legal_accidental_case_document',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='driver',
            name='pancard_front',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='driver',
            name='pancard_rear',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='driver',
            name='police_verification_front',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='driver',
            name='police_verification_rear',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='driver',
            name='votercard_front',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='driver',
            name='votercard_rear',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='vendor_cars',
            name='insurance_front',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='vendor_cars',
            name='insurance_rear',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='vendor_cars',
            name='permita_front',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='vendor_cars',
            name='permita_rear',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='vendor_cars',
            name='permitb_front',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='vendor_cars',
            name='permitb_rear',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='vendor_cars',
            name='pollution_certificate',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='vendor_cars',
            name='rc_front',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='vendor_cars',
            name='rc_rear',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='vendor_cars',
            name='touristpermit_front',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='vendor_cars',
            name='touristpermit_rear',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='vendorprofile',
            name='aadharcard_front',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='vendorprofile',
            name='aadharcard_rear',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='vendorprofile',
            name='driving_licence_front',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='vendorprofile',
            name='driving_licence_rear',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='vendorprofile',
            name='pancard',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='vendorprofile',
            name='votercard_front',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='vendorprofile',
            name='votercard_rear',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
