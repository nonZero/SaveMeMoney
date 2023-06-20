from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from expenses.api_views import ExpenseViewSet

router = routers.DefaultRouter()
router.register("expense", ExpenseViewSet)

urlpatterns = [
    path("", include("expenses.urls")),
    path("", include("django.contrib.auth.urls")),
    path("api/", include(router.urls)),
    path("admin/", admin.site.urls),
]
