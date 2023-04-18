import random

import tqdm
from django.core.management.base import BaseCommand
from faker import Faker

from expenses.models import Expense


class Command(BaseCommand):
    help = "Creates fake data :-)"

    def add_arguments(self, parser):
        parser.add_argument("n", type=int)

    def handle(self, n, *args, **options):
        f = Faker()
        for i in tqdm.tqdm(range(n)):
            Expense.objects.create(
                amount=random.randint(10, 10_000) / 10,
                title=f.sentence(),
                date=f.date_this_year(),
            )
