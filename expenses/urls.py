from django.urls import path
from rest_framework import routers

from . import views
from .api_views import ExpenseViewSet

app_name = "e"


urlpatterns = [
    path("random/", views.RandomExpenseView.as_view(), name="random"),
    path("demo/", views.MyDemoView.as_view(), name="demo"),
    path("name/", views.RandomNameView.as_view(), name="random_name"),
    path("foo/", views.FooView.as_view(), name="foo"),
    path("", views.ExpenseListView.as_view(), name="list"),
    path("create/", views.ExpenseCreateView.as_view(), name="create"),
    path("<int:pk>/", views.ExpenseDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", views.ExpenseUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", views.ExpenseDeleteView.as_view(), name="delete"),
]
