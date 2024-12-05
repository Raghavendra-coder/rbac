# Generated by Django 5.1.3 on 2024-12-05 13:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('role_and_permission', '0002_alter_role_permissions'),
        ('user', '0002_alter_user_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='role_and_permission.role'),
        ),
    ]
