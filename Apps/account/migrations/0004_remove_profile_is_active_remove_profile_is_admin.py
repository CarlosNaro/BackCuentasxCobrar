# Generated by Django 4.2.5 on 2023-10-28 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_rename_is_staff_profile_is_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='is_admin',
        ),
    ]
