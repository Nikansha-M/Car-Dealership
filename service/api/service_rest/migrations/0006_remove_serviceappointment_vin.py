# Generated by Django 4.0.3 on 2022-08-02 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service_rest', '0005_serviceappointment_completed_serviceappointment_vip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serviceappointment',
            name='vin',
        ),
    ]
