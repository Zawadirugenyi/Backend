# Generated by Django 5.0.6 on 2024-07-12 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0010_tenant_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenant',
            name='phone_number',
            field=models.CharField(max_length=12),
        ),
    ]