from django.urls import path

from .views import redirect_view

urlpatterns = [
    path("<str:short_code>/", redirect_view, name="shorts_redirect_view"),
]
