# Generated by Django 4.2 on 2025-02-15 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0003_alter_message_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='message',
            new_name='content_message',
        ),
    ]
