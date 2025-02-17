# Generated by Django 4.2 on 2025-02-15 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_chat', models.CharField(max_length=10)),
                ('name_chat', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_user', models.CharField(max_length=65)),
                ('message', models.CharField(max_length=500)),
                ('date', models.DateField()),
                ('id_chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='messenger.chat')),
            ],
        ),
    ]
