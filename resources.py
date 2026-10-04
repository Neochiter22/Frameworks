def add_resource(
    resources: list[dict],
    user_id: int,
    provider_id: int,
    name: str,
    resource_type: str,
) -> dict:
    resource_id = max(
        (resource["id"] for resource in resources),
        default=0,
    ) + 1
    resource = {
        "id": resource_id,
        "user_id": user_id,
        "provider_id": provider_id,
        "name": name,
        "type": resource_type,
    }
    resources.append(resource)
    return resource


def find_resources(resources: list[dict], query: str) -> list[dict]:
    query = query.lower()
    return [
        resource
        for resource in resources
        if query in resource["name"].lower()
        or query in resource["type"].lower()
    ]


def filter_resources_by_provider(
    resources: list[dict],
    provider_id: int,
) -> list[dict]:
    return [
        resource
        for resource in resources
        if resource["provider_id"] == provider_id
    ]


def sort_resources(resources: list[dict]) -> list[dict]:
    return sorted(
        resources,
        key=lambda resource: (
            resource["provider_id"],
            resource["name"].lower(),
        ),
    )


def get_resource(resources: list[dict], resource_id: int) -> dict | None:
    for resource in resources:
        if resource["id"] == resource_id:
            return resource
    return None
