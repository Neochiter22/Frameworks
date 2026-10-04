def add_expense(
    expenses: list[dict],
    user_id: int,
    resource_id: int,
    amount: float,
    expense_date: str,
) -> dict:
    if amount < 0:
        raise ValueError(
            "Сумма расхода не может быть отрицательной"
        )

    expense_id = max(
        (expense["id"] for expense in expenses),
        default=0,
    ) + 1
    expense = {
        "id": expense_id,
        "user_id": user_id,
        "resource_id": resource_id,
        "amount": round(amount, 2),
        "date": expense_date,
    }
    expenses.append(expense)
    return expense


def total_expenses(expenses: list[dict]) -> float:
    return round(
        sum(expense["amount"] for expense in expenses),
        2,
    )


def expenses_for_resource(
    expenses: list[dict],
    resource_id: int,
) -> list[dict]:
    return [
        expense
        for expense in expenses
        if expense["resource_id"] == resource_id
    ]


def filter_expenses_by_min_amount(
    expenses: list[dict],
    min_amount: float,
):
    for expense in expenses:
        if expense["amount"] >= min_amount:
            yield expense


def sort_expenses(expenses: list[dict]) -> list[dict]:
    return sorted(
        expenses,
        key=lambda expense: expense["amount"],
        reverse=True,
    )


def get_budget_status(total: float, limit: float) -> str:
    if total < limit:
        return (
            "Расходы ниже установленного лимита"
        )
    if total == limit:
        return (
            "Расходы равны установленному лимиту"
        )
    return "Лимит расходов превышен"
