from django.db import models


class Expense(models.Model):
    amount = models.DecimalField(decimal_places=2, max_digits=15)
    title = models.CharField(max_length=300)
    date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"[#{self.id}] {self.date} ${self.amount} {self.title}"
        # return self.title
