import random

import tqdm
from django.core.management.base import BaseCommand
from faker import Faker

from expenses.models import Expense


class Command(BaseCommand):
    help = "Creates fake data :-)"

    def add_arguments(self, parser):
        parser.add_argument("n", type=int)
        parser.add_argument("--delete", action="store_true", help="delete before adding")

    def handle(self, n, delete, *args, **options):
        if delete:
            Expense.objects.all().delete()
        f = Faker()
        for i in tqdm.tqdm(range(n)):
            Expense.objects.create(
                amount=random.randint(10, 10_000) / 10,
                title=f.sentence(),
                date=f.date_this_year(),
                description="\n".join(f.paragraph() for i in range(random.randint(2,5)))
            )
