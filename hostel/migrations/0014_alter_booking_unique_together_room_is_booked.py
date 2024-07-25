# Generated by Django 5.0.6 on 2024-07-25 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0013_remove_booking_unique_tenant_booking_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='room',
            name='is_booked',
            field=models.BooleanField(default=False),
        ),
    ]
