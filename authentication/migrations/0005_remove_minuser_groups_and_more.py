# Generated by Django 4.2 on 2025-02-10 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_minuser_groups_minuser_is_superuser_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='minuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='minuser',
            name='user_permissions',
        ),
        migrations.AlterField(
            model_name='minuser',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
