# Generated by Django 4.2 on 2023-04-06 19:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("apps", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ShortUrl",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=uuid.uuid4,
                        max_length=255,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("created", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "slug",
                    models.SlugField(
                        blank=True,
                        editable=False,
                        max_length=80,
                        null=True,
                        unique=True,
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "short_code",
                    models.CharField(blank=True, max_length=15, unique=True),
                ),
                ("url_original", models.URLField()),
                ("is_active", models.BooleanField(default=True)),
                ("visitor", models.PositiveIntegerField(default=0)),
                (
                    "application",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="short_urls",
                        to="apps.application",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="short_urls",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Short URL",
                "verbose_name_plural": "Short URLs",
                "ordering": ["-created"],
            },
        ),
    ]