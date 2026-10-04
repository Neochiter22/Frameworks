def add_provider(providers: list[dict], name: str) -> dict:
    provider_id = max(
        (provider["id"] for provider in providers),
        default=0,
    ) + 1
    provider = {
        "id": provider_id,
        "name": name,
    }
    providers.append(provider)
    return provider


def find_providers(providers: list[dict], query: str) -> list[dict]:
    query = query.lower()
    return [
        provider
        for provider in providers
        if query in provider["name"].lower()
    ]


def get_provider(providers: list[dict], provider_id: int) -> dict | None:
    for provider in providers:
        if provider["id"] == provider_id:
            return provider
    return None
