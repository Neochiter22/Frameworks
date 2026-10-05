from models import Provider


def add_provider(providers: list[Provider], name: str) -> Provider:
    provider_id = max(
        (provider.id for provider in providers),
        default=0,
    ) + 1
    provider = Provider(provider_id, name)
    providers.append(provider)
    return provider


def find_providers(
    providers: list[Provider],
    query: str,
) -> list[Provider]:
    query = query.lower()
    return [
        provider
        for provider in providers
        if query in provider.name.lower()
    ]


def get_provider(
    providers: list[Provider],
    provider_id: int,
) -> Provider | None:
    for provider in providers:
        if provider.id == provider_id:
            return provider
    return None
