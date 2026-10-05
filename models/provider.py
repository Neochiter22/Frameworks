from .entity import Entity


class Provider(Entity):
    def __init__(self, provider_id: int, name: str) -> None:
        super().__init__(provider_id)
        self.name = name

    def __str__(self) -> str:
        return f"{self.id}: {self.name}"

    @classmethod
    def from_data(cls, data: dict) -> "Provider":
        return cls(
            provider_id=data["id"],
            name=data["name"],
        )

    def to_data(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
        }
