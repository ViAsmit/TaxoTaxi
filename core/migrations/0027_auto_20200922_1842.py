# Generated by Django 2.2 on 2020-09-22 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_auto_20200907_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='final_ride_detail',
            name='amount_paid',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='final_ride_detail',
            name='itr_deduction',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='final_ride_detail',
            name='payment_reference',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]