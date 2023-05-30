from django import forms

from expenses.models import Expense


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = "__all__"


class ConfirmDeleteView(forms.Form):
    are_you_sure = forms.BooleanField()
