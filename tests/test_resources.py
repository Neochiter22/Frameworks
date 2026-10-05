from models import Provider, Resource, User
from resources import (
    add_resource,
    filter_resources_by_provider,
    get_resource,
    sort_resources,
)


def make_objects() -> tuple[User, Provider, Provider]:
    user = User(1, "Никита", "nikita@example.com")
    yandex = Provider(1, "Yandex Cloud")
    selectel = Provider(2, "Selectel")
    return user, yandex, selectel


def test_add_resource_creates_object() -> None:
    user, provider, _ = make_objects()
    resources = []

    resource = add_resource(
        resources,
        user,
        provider,
        "web-server",
        "virtual_machine",
    )

    assert isinstance(resource, Resource)
    assert resource.user is user
    assert resource.provider is provider
    assert get_resource(resources, 1) is resource


def test_filter_resources_by_provider() -> None:
    user, yandex, selectel = make_objects()
    resources = [
        Resource(1, user, yandex, "web-server", "virtual_machine"),
        Resource(2, user, selectel, "backup", "object_storage"),
    ]

    result = filter_resources_by_provider(resources, 2)

    assert result == [resources[1]]


def test_sort_resources() -> None:
    user, yandex, selectel = make_objects()
    resources = [
        Resource(2, user, selectel, "backup", "object_storage"),
        Resource(1, user, yandex, "web-server", "virtual_machine"),
    ]

    result = sort_resources(resources)

    assert result == [resources[1], resources[0]]


def test_resource_to_data() -> None:
    user, provider, _ = make_objects()
    resource = Resource(
        1,
        user,
        provider,
        "web-server",
        "virtual_machine",
    )

    assert resource.to_data() == {
        "id": 1,
        "user_id": 1,
        "provider_id": 1,
        "name": "web-server",
        "type": "virtual_machine",
    }
