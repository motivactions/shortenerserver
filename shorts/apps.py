from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.utils.translation import gettext_lazy as _


class ShortsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "shorts"
    label = "shorts"
    verbose_name = _("Shorts")

    def ready(self):
        post_migrate.connect(init_app, sender=self)
        return super().ready()


def init_app(sender, **kwargs):
    """For initializations"""
    pass
