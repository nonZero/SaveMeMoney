from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404

from expenses.models import Expense


def expense_list_view(request: HttpRequest):
    qs = Expense.objects.all()
    return render(
        request,
        "expenses/expense_list.html",
        {
            "object_list": qs,
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
