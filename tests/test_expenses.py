import pytest

from expenses import (
    add_expense,
    filter_expenses_by_min_amount,
    get_budget_status,
    total_expenses,
)
from models import Expense, Provider, Resource, User


def make_resource() -> tuple[User, Resource]:
    user = User(1, "Никита", "nikita@example.com")
    provider = Provider(1, "Yandex Cloud")
    resource = Resource(
        1,
        user,
        provider,
        "web-server",
        "virtual_machine",
    )
    return user, resource


def test_add_expense_creates_object() -> None:
    user, resource = make_resource()
    expenses = []

    expense = add_expense(
        expenses,
        user,
        resource,
        1450.5,
        "2026-10-01",
    )

    assert isinstance(expense, Expense)
    assert expense.resource is resource
    assert expense.user is user
    assert expense.amount == 1450.5


def test_negative_expense_is_rejected() -> None:
    user, resource = make_resource()

    with pytest.raises(ValueError):
        Expense(1, user, resource, -1, "2026-10-01")


def test_amount_property_validates_new_value() -> None:
    user, resource = make_resource()
    expense = Expense(1, user, resource, 100, "2026-10-01")

    with pytest.raises(ValueError):
        expense.amount = -50


def test_total_expenses() -> None:
    user, resource = make_resource()
    expenses = [
        Expense(1, user, resource, 100, "2026-10-01"),
        Expense(2, user, resource, 50.5, "2026-10-02"),
    ]

    assert total_expenses(expenses) == 150.5


def test_filter_expenses_by_min_amount() -> None:
    user, resource = make_resource()
    expenses = [
        Expense(1, user, resource, 100, "2026-10-01"),
        Expense(2, user, resource, 500, "2026-10-02"),
    ]

    result = list(filter_expenses_by_min_amount(expenses, 200))

    assert result == [expenses[1]]


def test_budget_status() -> None:
    assert get_budget_status(100, 200) == (
        "Расходы ниже установленного лимита"
    )
    assert get_budget_status(200, 200) == (
        "Расходы равны установленному лимиту"
    )
    assert get_budget_status(300, 200) == "Лимит расходов превышен"
