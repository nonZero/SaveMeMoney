from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from expenses import models
from expenses.serializers import ExpenseSerializer


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = models.Expense.objects.all()
    serializer_class = ExpenseSerializer

    ...
