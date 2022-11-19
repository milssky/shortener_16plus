from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("go/<slug:slug>", views.go_to_full_url, name="go")
]