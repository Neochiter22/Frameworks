import json
from pathlib import Path

from models import Expense, Provider, Resource, User

Serializable = User | Provider | Resource | Expense


def load_json(filename: str, default: list[dict]) -> list[dict]:
    path = Path(filename)
    try:
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return default
    except json.JSONDecodeError:
        print(f"Ошибка чтения JSON: {filename}")
        return default


def load_users(filename: str) -> list[User]:
    return [User.from_data(data) for data in load_json(filename, [])]


def load_providers(filename: str) -> list[Provider]:
    return [Provider.from_data(data) for data in load_json(filename, [])]


def load_resources(
    filename: str,
    users: list[User],
    providers: list[Provider],
) -> list[Resource]:
    users_by_id = {user.id: user for user in users}
    providers_by_id = {
        provider.id: provider for provider in providers
    }
    resources = []

    for data in load_json(filename, []):
        try:
            resource = Resource.from_data(
                data,
                users_by_id,
                providers_by_id,
            )
            resources.append(resource)
        except ValueError as error:
            print(f"Ошибка загрузки ресурса: {error}")

    return resources


def load_expenses(
    filename: str,
    users: list[User],
    resources: list[Resource],
) -> list[Expense]:
    users_by_id = {user.id: user for user in users}
    resources_by_id = {
        resource.id: resource for resource in resources
    }
    expenses = []

    for data in load_json(filename, []):
        try:
            expense = Expense.from_data(
                data,
                users_by_id,
                resources_by_id,
            )
            expenses.append(expense)
        except ValueError as error:
            print(f"Ошибка загрузки расхода: {error}")

    return expenses


def save_objects(
    filename: str,
    objects: list[Serializable],
) -> None:
    path = Path(filename)
    path.parent.mkdir(parents=True, exist_ok=True)
    data = [obj.to_data() for obj in objects]

    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
