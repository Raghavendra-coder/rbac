# Generated by Django 5.1.3 on 2024-12-05 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('role_and_permission', '0004_remove_role_permissions_role_permissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='is_default',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
