# Generated by Django 5.0.6 on 2024-06-17 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0002_remove_room_type_notification_tenant_room_room_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenant',
            name='password',
            field=models.CharField(default='default_password', max_length=255),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.CharField(choices=[('bedsitter', 'Bedsitter'), ('one_bedroom', 'One Bedroom'), ('two_bedrooms', 'Two Bedrooms'), ('three_bedrooms', 'Three Bedrooms')], default='bedsitter', max_length=50),
        ),
    ]
