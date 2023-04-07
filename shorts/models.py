import uuid
import logging
from random import choice
from string import ascii_letters, digits

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import translation, timezone
from django.urls import reverse
from apps.models import Application

from .managers import ShortUrlManager
from .utils import unique_slugify

_ = translation.gettext_lazy

SIZE = getattr(settings, "MAXIMUM_URL_CHARS", 7)

AVAIABLE_CHARS = ascii_letters + digits

logger = logging.getLogger(__name__)

User = get_user_model()


class ShortUrl(models.Model):
    id = models.CharField(
        max_length=255,
        default=uuid.uuid4,
        primary_key=True,
        unique=True,
    )
    created = models.DateTimeField(default=timezone.now)
    application = models.ForeignKey(
        Application,
        null=True,
        blank=True,
        related_name="short_urls",
        on_delete=models.SET_NULL,
    )
    user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        related_name="short_urls",
        on_delete=models.SET_NULL,
    )
    slug = models.SlugField(
        unique=True,
        null=True,
        blank=True,
        editable=False,
        max_length=80,
    )
    title = models.CharField(max_length=255)
    description = models.TextField(
        null=True,
        blank=True,
    )
    short_code = models.CharField(
        max_length=15,
        unique=True,
        blank=True,
    )
    url_original = models.URLField()
    is_active = models.BooleanField(default=True)
    visitor = models.PositiveIntegerField(default=0)

    objects = ShortUrlManager()

    class Meta:
        ordering = ["-created"]
        verbose_name = _("Short URL")
        verbose_name_plural = _("Short URLs")

    def __str__(self):
        return f"{self.url_original} to {self.short_code}"

    def create_random_code(self):
        """
        Creates a random string with the predetermined size
        """
        return "".join([choice(AVAIABLE_CHARS) for _ in range(SIZE)])

    def create_short_code(self):
        random_code = self.create_random_code()
        model_class = self.__class__
        if model_class.objects.filter(short_code=random_code).exists():
            return self.create_shortened_url(self)

        return random_code

    @property
    def opts(self):
        return self.__class__._meta

    def get_absolute_url(self):
        path = reverse("shorts_redirect_view", kwargs={"short_code": self.short_code})
        return f"{settings.BASE_URL}{path}"

    def save(self, *args, **kwargs):
        # If the short url wasn't specified
        if not self.short_code:
            # We pass the model instance that is being saved
            self.short_code = self.create_short_code()
        if not self.slug:
            unique_slugify(self, self.title)
        super().save(*args, **kwargs)
