from models import User
from users import add_user, find_users, get_user


def test_user_from_data() -> None:
    user = User.from_data(
        {"id": 1, "name": "Никита", "email": "nikita@example.com"}
    )

    assert user.id == 1
    assert user.name == "Никита"
    assert user.email == "nikita@example.com"


def test_add_user_creates_object() -> None:
    users = []

    user = add_user(users, "Никита", "nikita@example.com")

    assert isinstance(user, User)
    assert users == [user]
    assert get_user(users, 1) is user


def test_find_users() -> None:
    users = [
        User(1, "Никита Евтенко", "nikita@example.com"),
        User(2, "Иван Петров", "ivan@example.com"),
    ]

    assert find_users(users, "евтенко") == [users[0]]
    assert find_users(users, "ivan") == [users[1]]
