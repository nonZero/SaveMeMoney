import random

import tqdm
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from faker import Faker

from expenses.models import Expense, Category


class Command(BaseCommand):
    help = "Creates fake data :-)"

    def add_arguments(self, parser):
        parser.add_argument("n", type=int)
        parser.add_argument(
            "--delete", action="store_true", help="delete before adding"
        )

    def handle(self, n, delete, *args, **options):
        f = Faker()
        if delete:
            Expense.objects.all().delete()
            Category.objects.all().delete()

        for i in range(1, 6):
            User.objects.create_user(username=f"user{i}", password="xyzzy")

        users = list(User.objects.all())

        for c in "food utilities fun other house education".split():
            Category.objects.get_or_create(name=c.title())

        cats = list(Category.objects.all())

        for i in tqdm.tqdm(range(n)):
            Expense.objects.create(
                owner=random.choice(users),
                amount=random.randint(10, 10_000) / 10,
                title=f.sentence(),
                date=f.date_this_year(),
                category=random.choice(cats),
                description="\n".join(
                    f.paragraph() for i in range(random.randint(2, 5))
                ),
            )
