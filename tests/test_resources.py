from resources import (
    add_resource,
    filter_resources_by_provider,
    find_resources,
    sort_resources,
)


def test_add_resource():
    resources = []
    resource = add_resource(resources, 1, 2, "db", "database")
    assert resource["id"] == 1
    assert resource["provider_id"] == 2


def test_find_resources():
    resources = [
        {
            "id": 1,
            "user_id": 1,
            "provider_id": 1,
            "name": "web-server",
            "type": "virtual_machine",
        }
    ]
    result = find_resources(resources, "WEB")
    assert len(result) == 1


def test_filter_resources_by_provider():
    resources = [
        {"id": 1, "provider_id": 1, "name": "a"},
        {"id": 2, "provider_id": 2, "name": "b"},
    ]
    result = filter_resources_by_provider(resources, 2)
    assert [resource["id"] for resource in result] == [2]


def test_sort_resources():
    resources = [
        {"id": 1, "provider_id": 2, "name": "z"},
        {"id": 2, "provider_id": 1, "name": "b"},
        {"id": 3, "provider_id": 1, "name": "a"},
    ]
    result = sort_resources(resources)
    assert [resource["id"] for resource in result] == [3, 2, 1]
