from django.conf import settings
from django.shortcuts import  get_object_or_404, redirect, render

from .forms import UrlForm
from .models import Url
from .utils import get_unique_slug


def index(request):
    form = UrlForm(request.POST or None)
    if not form.is_valid():
        return render(request, "shortener/index.html", {"form": form})
    
    short_url = form.save(commit=False)
    short_url.slug = get_unique_slug()
    short_url.save()

    return render(
        request, 
        "shortener/index.html", 
        {
            "form": form,
            "short_url": f"{settings.SITE_URL}go/{short_url.slug}"
        }
    )


def go_to_full_url(request, slug):
    short_url = get_object_or_404(Url, slug=slug)
    short_url.nums_of_visits += 1
    short_url.save()
    return redirect(short_url.full_url, permanent=True)
