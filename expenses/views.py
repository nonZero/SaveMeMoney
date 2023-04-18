import random

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from expenses.models import Expense


def expense_list_view(request: HttpRequest):
    qs = Expense.objects.all()
    number_of_expenses = Expense.objects.count()
    u = {"name": "udi", "phone": "555-55555"}
    e = Expense.objects.order_by("?").first()
    return render(
        request,
        "expenses/expense_list.html",
        {
            "object_list": qs,
            "n": number_of_expenses,
            "r": random.randint(1, 100),
            "nums": random.choices(range(100), k=5),
            "u": u,
            "e": e,
        },
    )
