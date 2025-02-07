# Generated by Django 5.1.5 on 2025-02-05 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rms', '0004_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('P', 'Pending'), ('C', 'Completed')], default='P', max_length=1),
        ),
    ]
