from models import User


def add_user(users: list[User], name: str, email: str) -> User:
    user_id = max((user.id for user in users), default=0) + 1
    user = User(user_id, name, email)
    users.append(user)
    return user


def find_users(users: list[User], query: str) -> list[User]:
    query = query.lower()
    return [
        user
        for user in users
        if query in user.name.lower() or query in user.email.lower()
    ]


def get_user(users: list[User], user_id: int) -> User | None:
    for user in users:
        if user.id == user_id:
            return user
    return None
