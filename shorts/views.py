# views.py
from django.http import Http404
from django.shortcuts import render

from .models import ShortUrl

template = "shorts/redirect.html"


def redirect_view(request, short_code):
    # TODO Visitor count per ip/day
    # TODO Rate limiting
    try:
        shortener = ShortUrl.objects.get(
            short_code=short_code,
            is_active=True,
        )
        shortener.visitor += 1
        shortener.save()
        context = {"url_original": shortener.url_original}
        return render(request, template, context)
    except ShortUrl.DoesNotExist:
        raise Http404("Sorry this link is broken :(")
