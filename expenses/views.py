from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from expenses.forms import ExpenseForm
from expenses.models import Expense


class FooView(View):
    def get(self, request, *args, **kwargs):
        assert False, "yo!!!"


class ExpenseListView(ListView):
    model = Expense
    ordering = "-date"
    paginate_by = 15

    def get_queryset(self):
        qs = super().get_queryset()
        if q := self.request.GET.get("q"):
            qs = qs.filter(title__icontains=q)
        return qs


class ExpenseDetailView(DetailView):
    model = Expense


class ExpenseCreateView(SuccessMessageMixin, CreateView):
    model = Expense
    form_class = ExpenseForm
    success_message = "Expense %(title)s added successfully."


class ExpenseUpdateView(SuccessMessageMixin, UpdateView):
    model = Expense
    form_class = ExpenseForm
    success_message = "Expense %(title)s updated successfully."

    # def form_valid(self, form):
    #     resp = super().form_valid(form)
    #     messages.info(self.request, f"Expense #{self.object.id} added successfully.")
    #     return resp


class ExpenseDeleteView(SuccessMessageMixin, DeleteView):
    model = Expense
    success_url = reverse_lazy("e:list")

    def get_success_message(self, cleaned_data):
        return f"Expense #{self.kwargs['pk']} deleted successfully."
