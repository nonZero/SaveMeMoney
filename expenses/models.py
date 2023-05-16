from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=300, unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

class Expense(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(decimal_places=2, max_digits=15)
    title = models.CharField(max_length=300)
    date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="expenses")
    description = models.TextField(blank=True)

    def __str__(self):
        return f"[#{self.id}] {self.date} ${self.amount} {self.title}"
        # return self.title

    def is_expensive(self):
        return self.amount > 200
