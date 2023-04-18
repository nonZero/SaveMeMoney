import pytest
from django.test.client import Client

from expenses.models import Expense


def test_add_100_200(client: Client):
    resp = client.get("/add/100/200/")
    assert resp.status_code == 200
    assert "<b>300</b>" in resp.content.decode()


def test_multiply_100_200(client: Client):
    resp = client.get("/mult/5/6/")
    assert resp.status_code == 200
    assert "5 * 6 = 30" == resp.content.decode()
