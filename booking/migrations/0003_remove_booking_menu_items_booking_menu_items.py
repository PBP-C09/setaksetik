# Generated by Django 5.1.1 on 2024-10-24 01:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_remove_booking_status'),
        ('explore', '0002_auto_20241015_1150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='menu_items',
        ),
        migrations.AddField(
            model_name='booking',
            name='menu_items',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='explore.menu'),
            preserve_default=False,
        ),
    ]
