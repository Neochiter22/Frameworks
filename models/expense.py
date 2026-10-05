from .entity import Entity
from .resource import Resource
from .user import User


class Expense(Entity):
    def __init__(
        self,
        expense_id: int,
        user: User,
        resource: Resource,
        amount: float,
        expense_date: str,
    ) -> None:
        super().__init__(expense_id)
        self.user = user
        self.resource = resource
        self.amount = amount
        self.date = expense_date

    @property
    def amount(self) -> float:
        return self._amount

    @amount.setter
    def amount(self, value: float) -> None:
        if not self.validate_amount(value):
            raise ValueError("Сумма расхода не может быть отрицательной")
        self._amount = round(value, 2)

    @staticmethod
    def validate_amount(amount: float) -> bool:
        return amount >= 0

    def __str__(self) -> str:
        return (
            f"{self.id}: {self.resource.name} | {self.date} | "
            f"{self.amount:.2f} руб."
        )

    @classmethod
    def from_data(
        cls,
        data: dict,
        users: dict[int, User],
        resources: dict[int, Resource],
    ) -> "Expense":
        user = users.get(data["user_id"])
        resource = resources.get(data["resource_id"])

        if user is None:
            raise ValueError("Пользователь расхода не найден")
        if resource is None:
            raise ValueError("Ресурс расхода не найден")

        return cls(
            expense_id=data["id"],
            user=user,
            resource=resource,
            amount=data["amount"],
            expense_date=data["date"],
        )

    def to_data(self) -> dict:
        return {
            "id": self.id,
            "user_id": self.user.id,
            "resource_id": self.resource.id,
            "amount": self.amount,
            "date": self.date,
        }
