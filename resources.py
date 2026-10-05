from models import Provider, Resource, User


def add_resource(
    resources: list[Resource],
    user: User,
    provider: Provider,
    name: str,
    resource_type: str,
) -> Resource:
    resource_id = max(
        (resource.id for resource in resources),
        default=0,
    ) + 1
    resource = Resource(
        resource_id,
        user,
        provider,
        name,
        resource_type,
    )
    resources.append(resource)
    return resource


def find_resources(
    resources: list[Resource],
    query: str,
) -> list[Resource]:
    query = query.lower()
    return [
        resource
        for resource in resources
        if query in resource.name.lower()
        or query in resource.resource_type.lower()
    ]


def filter_resources_by_provider(
    resources: list[Resource],
    provider_id: int,
) -> list[Resource]:
    return [
        resource
        for resource in resources
        if resource.provider.id == provider_id
    ]


def sort_resources(resources: list[Resource]) -> list[Resource]:
    return sorted(
        resources,
        key=lambda resource: (
            resource.provider.id,
            resource.name.lower(),
        ),
    )


def get_resource(
    resources: list[Resource],
    resource_id: int,
) -> Resource | None:
    for resource in resources:
        if resource.id == resource_id:
            return resource
    return None
