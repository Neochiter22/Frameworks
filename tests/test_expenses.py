import pytest

from expenses import (
    add_expense,
    filter_expenses_by_min_amount,
    get_budget_status,
    sort_expenses,
    total_expenses,
)


def test_add_expense():
    expenses = []
    expense = add_expense(expenses, 1, 3, 99.999, "2026-10-04")
    assert expense["amount"] == 100.0
    assert expense["id"] == 1


def test_negative_expense_rejected():
    with pytest.raises(ValueError):
        add_expense([], 1, 1, -1.0, "2026-10-04")


def test_total_expenses():
    expenses = [{"amount": 100.0}, {"amount": 25.5}]
    assert total_expenses(expenses) == 125.5


def test_filter_expenses_generator():
    expenses = [
        {"id": 1, "amount": 100.0},
        {"id": 2, "amount": 500.0},
    ]
    result = list(filter_expenses_by_min_amount(expenses, 200.0))
    assert [expense["id"] for expense in result] == [2]


def test_sort_expenses():
    expenses = [
        {"id": 1, "amount": 100.0},
        {"id": 2, "amount": 500.0},
    ]
    result = sort_expenses(expenses)
    assert [expense["id"] for expense in result] == [2, 1]


def test_budget_status():
    assert get_budget_status(900.0, 1000.0) == (
        "Расходы ниже установленного лимита"
    )
