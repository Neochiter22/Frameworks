from .entity import Entity
from .provider import Provider
from .user import User


class Resource(Entity):
    def __init__(
        self,
        resource_id: int,
        user: User,
        provider: Provider,
        name: str,
        resource_type: str,
    ) -> None:
        super().__init__(resource_id)
        self.user = user
        self.provider = provider
        self.name = name
        self.resource_type = resource_type

    def __str__(self) -> str:
        return (
            f"{self.id}: {self.name} | {self.resource_type} | "
            f"{self.provider.name} | user_id={self.user.id}"
        )

    @classmethod
    def from_data(
        cls,
        data: dict,
        users: dict[int, User],
        providers: dict[int, Provider],
    ) -> "Resource":
        user = users.get(data["user_id"])
        provider = providers.get(data["provider_id"])

        if user is None:
            raise ValueError("Пользователь ресурса не найден")
        if provider is None:
            raise ValueError("Провайдер ресурса не найден")

        return cls(
            resource_id=data["id"],
            user=user,
            provider=provider,
            name=data["name"],
            resource_type=data["type"],
        )

    def to_data(self) -> dict:
        return {
            "id": self.id,
            "user_id": self.user.id,
            "provider_id": self.provider.id,
            "name": self.name,
            "type": self.resource_type,
        }
