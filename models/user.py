from .entity import Entity


class User(Entity):
    def __init__(self, user_id: int, name: str, email: str) -> None:
        super().__init__(user_id)
        self.name = name
        self.email = email

    def __str__(self) -> str:
        return f"{self.id}: {self.name} <{self.email}>"

    @classmethod
    def from_data(cls, data: dict) -> "User":
        return cls(
            user_id=data["id"],
            name=data["name"],
            email=data["email"],
        )

    def to_data(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
        }
