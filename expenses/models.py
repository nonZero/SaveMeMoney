from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=300, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=300, unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Expense(models.Model):
    owner = models.ForeignKey(User, on_delete=models.PROTECT, related_name="expenses")
    created_at = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(decimal_places=2, max_digits=15)
    title = models.CharField(max_length=300)
    date = models.DateField()
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name="expenses"
    )
    tags = models.ManyToManyField(Tag, related_name="tags", blank=True)
    description = models.TextField(blank=True)
    is_starred = models.BooleanField(default=False)

    def __str__(self):
        return f"[#{self.id}] {self.date} ${self.amount} {self.title}"

    def get_absolute_url(self):
        return reverse("e:detail", args=(self.id,))

    def is_expensive(self):
        return self.amount > 200


# class FavouriteExpense(models.Model):
#     expense = models.ForeignKey(Expense, ...)
#     user = models.ForeignKey(User, ...)
#     starred_at = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         unique_together = (("expense", "user"),)
