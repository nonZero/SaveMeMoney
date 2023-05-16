from django.urls import path

from . import views

app_name = "e"

urlpatterns = [
    path("", views.expense_list_view, name="list"),
    path("<int:pk>/", views.expense_detail_view, name="detail"),
]
