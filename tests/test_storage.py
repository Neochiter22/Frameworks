import json

from models import Expense, Provider, Resource, User
from storage import (
    load_expenses,
    load_providers,
    load_resources,
    load_users,
    save_objects,
)


def test_load_objects_and_links(tmp_path) -> None:
    users_file = tmp_path / "users.json"
    providers_file = tmp_path / "providers.json"
    resources_file = tmp_path / "resources.json"
    expenses_file = tmp_path / "expenses.json"

    users_file.write_text(
        json.dumps(
            [{"id": 1, "name": "Никита", "email": "n@example.com"}]
        ),
        encoding="utf-8",
    )
    providers_file.write_text(
        json.dumps([{"id": 1, "name": "Yandex Cloud"}]),
        encoding="utf-8",
    )
    resources_file.write_text(
        json.dumps(
            [
                {
                    "id": 1,
                    "user_id": 1,
                    "provider_id": 1,
                    "name": "web-server",
                    "type": "virtual_machine",
                }
            ]
        ),
        encoding="utf-8",
    )
    expenses_file.write_text(
        json.dumps(
            [
                {
                    "id": 1,
                    "user_id": 1,
                    "resource_id": 1,
                    "amount": 100,
                    "date": "2026-10-01",
                }
            ]
        ),
        encoding="utf-8",
    )

    users = load_users(str(users_file))
    providers = load_providers(str(providers_file))
    resources = load_resources(str(resources_file), users, providers)
    expenses = load_expenses(str(expenses_file), users, resources)

    assert isinstance(users[0], User)
    assert isinstance(providers[0], Provider)
    assert isinstance(resources[0], Resource)
    assert isinstance(expenses[0], Expense)
    assert resources[0].user is users[0]
    assert resources[0].provider is providers[0]
    assert expenses[0].resource is resources[0]


def test_save_objects(tmp_path) -> None:
    filename = tmp_path / "users.json"
    users = [User(1, "Никита", "nikita@example.com")]

    save_objects(str(filename), users)

    data = json.loads(filename.read_text(encoding="utf-8"))
    assert data == [
        {
            "id": 1,
            "name": "Никита",
            "email": "nikita@example.com",
        }
    ]
