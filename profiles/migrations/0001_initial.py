# Generated by Django 5.1.2 on 2024-10-23 13:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.CreateModel(
                    name='Profile',
                    fields=[
                        ('id', models.BigAutoField(auto_created=True,
                         primary_key=True, serialize=False, verbose_name='ID')),
                        ('favorite_city', models.CharField(blank=True, max_length=64)),
                        ('user', models.OneToOneField(
                            on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                    ],
                ),
            ],
            # Table already exists. See oc_lettings_site/migrations/0003_delete_profile.py
            database_operations=[],
        ),
    ]