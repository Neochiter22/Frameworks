from collections.abc import Iterator

from models import Expense, Resource, User


def add_expense(
    expenses: list[Expense],
    user: User,
    resource: Resource,
    amount: float,
    expense_date: str,
) -> Expense:
    expense_id = max(
        (expense.id for expense in expenses),
        default=0,
    ) + 1
    expense = Expense(
        expense_id,
        user,
        resource,
        amount,
        expense_date,
    )
    expenses.append(expense)
    return expense


def total_expenses(expenses: list[Expense]) -> float:
    return round(sum(expense.amount for expense in expenses), 2)


def expenses_for_resource(
    expenses: list[Expense],
    resource_id: int,
) -> list[Expense]:
    return [
        expense
        for expense in expenses
        if expense.resource.id == resource_id
    ]


def filter_expenses_by_min_amount(
    expenses: list[Expense],
    min_amount: float,
) -> Iterator[Expense]:
    for expense in expenses:
        if expense.amount >= min_amount:
            yield expense


def sort_expenses(expenses: list[Expense]) -> list[Expense]:
    return sorted(
        expenses,
        key=lambda expense: expense.amount,
        reverse=True,
    )


def get_budget_status(total: float, limit: float) -> str:
    if total < limit:
        return "Расходы ниже установленного лимита"
    if total == limit:
        return "Расходы равны установленному лимиту"
    return "Лимит расходов превышен"
