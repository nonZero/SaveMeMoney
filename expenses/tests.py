import pytest

from expenses.models import Expense


@pytest.mark.django_db
def test_create_expense():
    Expense.objects.create(
        amount="12.34",
        title="pizza",
        date="2022-10-25",
    )
    assert Expense.objects.count() == 1
