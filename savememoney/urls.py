"""
URL configuration for savememoney project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import random

from django.contrib import admin
from django.http import HttpResponse, HttpRequest, JsonResponse, HttpResponseNotAllowed
from django.urls import path


def my_view(request):
    a = 239487324
    b = 3298473
    c = a * b
    return HttpResponse(f"c is {c}")


def birthday(request: HttpRequest, name: str, age: int):
    if name == "shooki":
        return HttpResponseNotAllowed("no!")
    return HttpResponse(f"{name.upper()} is {age} years old.")


def add_view(request, a: int, b: int):
    return HttpResponse(f"{a} + {b} = <b>{a + b}</b>")


def multiply_view(request, a: int, b: int):
    return HttpResponse(f"{a} * {b} = {a * b}")


def api_add_view(request, a: int, b: int):
    return JsonResponse(
        {
            "result": a + b,
            "surprise": random.randint(1, 100),
        }
    )


urlpatterns = [
    path("", my_view),
    path("age/<name>/<int:age>/", birthday),
    path("age/<int:age>/<name>/", birthday),
    path("add/<int:a>/<int:b>/", add_view),
    path("mult/<int:a>/<int:b>/", multiply_view),
    path("api/add/<int:a>/<int:b>/", api_add_view),
    path("admin/", admin.site.urls),
]
