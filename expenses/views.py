from django import forms
from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from expenses.models import Expense


def expense_list_view(request: HttpRequest):
    qs = Expense.objects.all()
    if q := request.GET.get("q"):
        qs = qs.filter(title__icontains=q)

    return render(
        request,
        "expenses/expense_list.html",
        {
            "object_list": qs,
        },
    )


# class IceCreamForm(forms.Form):
#     number_of_cones = forms.IntegerField()
#     cream = forms.BooleanField(required=False)
#     customer_name = forms.CharField()
#     email_for_reciept = forms.EmailField()
#     comments = forms.CharField(widget=forms.Textarea, required=False)
#     date = forms.DateField()


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = "__all__"


def expense_create_view(request: HttpRequest):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            # o = Expense.objects.create(**form.cleaned_data)
            o = form.save()
            messages.info(request, f"Expense #{o.id} added successfully.")
            return redirect(reverse("e:detail", args=(o.id,)))

    else:
        form = ExpenseForm()
    return render(
        request,
        "expenses/expense_form.html",
        {
            "form": form,
        },
    )


def expense_update_view(request: HttpRequest, pk: int):
    o = get_object_or_404(Expense, pk=pk)
    if request.method == "POST":
        form = ExpenseForm(instance=o, data=request.POST)
        if form.is_valid():
            # o = Expense.objects.create(**form.cleaned_data)
            o = form.save()
            messages.info(request, f"Expense #{o.id} saved successfully.")
            return redirect(reverse("e:detail", args=(o.id,)))

    else:
        form = ExpenseForm(instance=o)
    return render(
        request,
        "expenses/expense_form.html",
        {
            "form": form,
        },
    )


class ConfirmDeleteView(forms.Form):
    are_you_sure = forms.BooleanField()


def expense_delete_view(request: HttpRequest, pk: int):
    o = get_object_or_404(Expense, pk=pk)
    if request.method == "POST":
        form = ConfirmDeleteView(data=request.POST)
        if form.is_valid():
            oid = o.id
            o.delete()
            messages.info(request, f"Expense #{oid} deleted successfully.")
            return redirect(reverse("e:list"))

    else:
        form = ConfirmDeleteView()
    return render(
        request,
        "expenses/expense_confirm_delete.html",
        {
            "form": form,
            "object": o,
        },
    )


def expense_detail_view(request: HttpRequest, pk: int):
    o = get_object_or_404(Expense, pk=pk)
    return render(
        request,
        "expenses/expense_detail.html",
        {
            "object": o,
        },
    )
