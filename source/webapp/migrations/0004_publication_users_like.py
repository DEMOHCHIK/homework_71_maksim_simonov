# Generated by Django 5.0.1 on 2024-01-20 15:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_publication_created'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='users_like',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
