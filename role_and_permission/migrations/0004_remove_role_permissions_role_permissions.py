# Generated by Django 5.1.3 on 2024-12-05 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('role_and_permission', '0003_alter_permissions_id_alter_role_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='role',
            name='permissions',
        ),
        migrations.AddField(
            model_name='role',
            name='permissions',
            field=models.ManyToManyField(blank=True, null=True, related_name='in_roles', to='role_and_permission.permissions'),
        ),
    ]
