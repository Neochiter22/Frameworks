def add_user(users: list[dict], name: str, email: str) -> dict:
    user_id = max((user["id"] for user in users), default=0) + 1
    user = {
        "id": user_id,
        "name": name,
        "email": email,
    }
    users.append(user)
    return user


def find_users(users: list[dict], query: str) -> list[dict]:
    query = query.lower()
    return [
        user
        for user in users
        if query in user["name"].lower()
        or query in user["email"].lower()
    ]


def get_user(users: list[dict], user_id: int) -> dict | None:
    for user in users:
        if user["id"] == user_id:
            return user
    return None
