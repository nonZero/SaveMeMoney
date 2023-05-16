from django.contrib import admin

from . import models


@admin.register(models.Category)
class ExpenseCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Expense)
class ExpenseModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "amount",
        "date",
        "created_at",
    )
    search_fields = (
        "id",
        "title",
        "amount",
    )
    date_hierarchy = "date"
    readonly_fields = ("created_at",)
