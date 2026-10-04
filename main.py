from datetime import date


def calculate_balance(income, expenses):
    return income - expenses


def get_budget_status(expenses, limit):
    if expenses < limit:
        return "Расходы ниже установленного лимита"
    if expenses == limit:
        return "Расходы равны установленному лимиту"
    return "Лимит расходов превышен"


def calculate_savings_rate(income, balance):
    if income <= 0:
        return 0.0
    return balance / income * 100


def is_finance_data_valid(income, expenses, limit):
    return income >= 0 and expenses >= 0 and limit >= 0


today = date.today()

print("Трекер личных финансов")
print(f"Дата расчёта: {today}")

income = float(input("Введите доход за месяц: "))
expenses = float(input("Введите расходы за месяц: "))
limit = float(input("Введите лимит расходов: "))

if is_finance_data_valid(income, expenses, limit):
    balance = calculate_balance(income, expenses)
    budget_status = get_budget_status(expenses, limit)
    savings_rate = calculate_savings_rate(income, balance)

    print(f"\nОстаток: {balance:.2f} руб.")
    print(budget_status)
    print(f"Доля остатка от дохода: {savings_rate:.1f}%")
else:
    print("Доход, расходы и лимит не могут быть отрицательными")
