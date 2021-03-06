# Generated by Django 2.2 on 2020-06-24 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0009_auto_20200621_1811'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bank_detail',
            options={'verbose_name_plural': 'Vendor Bank Details'},
        ),
        migrations.AlterField(
            model_name='bank_detail',
            name='account_holder_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='bank_detail',
            name='account_type',
            field=models.CharField(blank=True, choices=[('C', 'Current'), ('S', 'Saving')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='bank_detail',
            name='bank_address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
