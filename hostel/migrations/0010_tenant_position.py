# Generated by Django 5.0.6 on 2024-07-12 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0009_alter_tenant_nationality_alter_tenant_parent_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenant',
            name='position',
            field=models.CharField(default='exit', max_length=255),
            preserve_default=False,
        ),
    ]