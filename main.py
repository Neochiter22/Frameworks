from expenses import (
    add_expense,
    filter_expenses_by_min_amount,
    get_budget_status,
    sort_expenses,
    total_expenses,
)
from providers import add_provider, get_provider
from resources import (
    add_resource,
    filter_resources_by_provider,
    get_resource,
    sort_resources,
)
from storage import load_json, save_json
from users import add_user, get_user
from utils import input_date, input_float, input_int

USERS_FILE = "data/users.json"
PROVIDERS_FILE = "data/providers.json"
RESOURCES_FILE = "data/resources.json"
EXPENSES_FILE = "data/expenses.json"


def show_users(users: list[dict]) -> None:
    if not users:
        print("Пользователей пока нет")
        return

    for user in users:
        print(f'{user["id"]}: {user["name"]} <{user["email"]}>')


def show_providers(providers: list[dict]) -> None:
    if not providers:
        print("Провайдеров пока нет")
        return

    for provider in providers:
        print(f'{provider["id"]}: {provider["name"]}')


def show_resources(
    resources: list[dict],
    providers: list[dict],
) -> None:
    if not resources:
        print("Ресурсов пока нет")
        return

    for resource in sort_resources(resources):
        provider = get_provider(providers, resource["provider_id"])
        provider_name = (
            provider["name"] if provider else "Неизвестно"
        )
        print(
            f'{resource["id"]}: {resource["name"]} | '
            f'{resource["type"]} | {provider_name} | '
            f'user_id={resource["user_id"]}'
        )


def show_expenses(expenses: list[dict]) -> None:
    if not expenses:
        print("Расходов пока нет")
        return

    for expense in sort_expenses(expenses):
        print(
            f'{expense["id"]}: resource_id={expense["resource_id"]} | '
            f'{expense["date"]} | {expense["amount"]:.2f} руб.'
        )


def print_menu() -> None:
    print(
        "\n=== Система учёта облачных ресурсов ==="
    )
    print("1. Показать пользователей")
    print("2. Добавить пользователя")
    print("3. Показать провайдеров")
    print("4. Добавить провайдера")
    print("5. Показать ресурсы")
    print("6. Добавить ресурс")
    print("7. Ресурсы выбранного провайдера")
    print("8. Показать расходы")
    print("9. Добавить расход")
    print(
        "10. Показать расходы от указанной суммы"
    )
    print("11. Статистика расходов и лимит")
    print("0. Выход")


def main() -> None:
    users = load_json(USERS_FILE, [])
    providers = load_json(PROVIDERS_FILE, [])
    resources = load_json(RESOURCES_FILE, [])
    expenses = load_json(EXPENSES_FILE, [])

    while True:
        print_menu()
        choice = input("Выберите действие: ").strip()

        if choice == "0":
            break

        if choice == "1":
            show_users(users)

        elif choice == "2":
            name = input("Имя пользователя: ").strip()
            email = input("Email: ").strip()
            add_user(users, name, email)
            save_json(USERS_FILE, users)

        elif choice == "3":
            show_providers(providers)

        elif choice == "4":
            name = input("Название провайдера: ").strip()
            add_provider(providers, name)
            save_json(PROVIDERS_FILE, providers)

        elif choice == "5":
            show_resources(resources, providers)

        elif choice == "6":
            user_id = input_int("ID пользователя: ")
            provider_id = input_int("ID провайдера: ")

            if get_user(users, user_id) is None:
                print("Пользователь не найден")
                continue

            if get_provider(providers, provider_id) is None:
                print("Провайдер не найден")
                continue

            name = input("Название ресурса: ").strip()
            resource_type = input("Тип ресурса: ").strip()
            add_resource(
                resources,
                user_id,
                provider_id,
                name,
                resource_type,
            )
            save_json(RESOURCES_FILE, resources)

        elif choice == "7":
            provider_id = input_int("ID провайдера: ")
            selected = filter_resources_by_provider(
                resources,
                provider_id,
            )
            show_resources(selected, providers)

        elif choice == "8":
            show_expenses(expenses)

        elif choice == "9":
            user_id = input_int("ID пользователя: ")
            resource_id = input_int("ID ресурса: ")

            if get_user(users, user_id) is None:
                print("Пользователь не найден")
                continue

            resource = get_resource(resources, resource_id)
            if resource is None:
                print("Ресурс не найден")
                continue

            if resource["user_id"] != user_id:
                print(
                    "Ресурс принадлежит другому пользователю"
                )
                continue

            amount = input_float("Сумма расхода: ")
            expense_date = input_date("Дата (ДД.ММ.ГГГГ): ")
            add_expense(
                expenses,
                user_id,
                resource_id,
                amount,
                expense_date,
            )
            save_json(EXPENSES_FILE, expenses)

        elif choice == "10":
            min_amount = input_float("Минимальная сумма: ")
            selected = list(
                filter_expenses_by_min_amount(
                    expenses,
                    min_amount,
                )
            )
            show_expenses(selected)

        elif choice == "11":
            total = total_expenses(expenses)
            limit = input_float("Лимит расходов: ")
            print(f"Всего расходов: {total:.2f} руб.")
            print(get_budget_status(total, limit))

        else:
            print("Неизвестный пункт меню")


if __name__ == "__main__":
    main()
