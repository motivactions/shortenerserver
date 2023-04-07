from django.contrib import admin

from .models import ShortUrl


@admin.register(ShortUrl)
class ShortUrlAdmin(admin.ModelAdmin):
    list_display = ["title", "application", "user", "url_original", "shortened"]

    def shortened(self, obj):
        return obj.get_absolute_url()
