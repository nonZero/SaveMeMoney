from django.urls import path

from . import views

app_name = "e"

urlpatterns = [
    path("foo/", views.FooView.as_view(), name="foo"),
    path("", views.ExpenseListView.as_view(), name="list"),
    path("create/", views.ExpenseCreateView.as_view(), name="create"),
    path("<int:pk>/", views.ExpenseDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", views.ExpenseUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", views.ExpenseDeleteView.as_view(), name="delete"),
]
