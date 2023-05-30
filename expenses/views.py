from django import forms
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from expenses.models import Expense


def expense_list_view(request: HttpRequest):
    qs = Expense.objects.all()
    if q := request.GET.get("q"):
        qs = qs.filter(title__icontains=q)

    counter = int(request.COOKIES.get("counter", 0)) + 1
    hidden_counter = int(request.session.get("counter", 0)) + 1
    request.session["counter"] = hidden_counter
    r = render(
        request,
        "expenses/expense_list.html",
        {
            "object_list": qs,
            "counter": counter,
            "hiddent_counter": hidden_counter,
        },
    )
    r.cookies["counter"] = counter
    r.cookies["foo"] = "bar"
    r.cookies["theme"] = "dark"
    return r


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


def expense_detail_view(request: HttpRequest, pk: int):
    o = get_object_or_404(Expense, pk=pk)
    return render(
        request,
        "expenses/expense_detail.html",
        {
            "object": o,
        },
    )
