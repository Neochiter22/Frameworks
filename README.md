# Система учёта облачных ресурсов

Консольное приложение для учёта пользователей, облачных ресурсов,
провайдеров и расходов на облачную инфраструктуру.

## ПР3

В ПР3 проект из ПР2 переведён с коллекций словарей на объектную модель.
Основная функциональность ПР2 сохранена.

## Классы

### Entity

Базовый класс предметных сущностей.

Атрибут:

- `id` — идентификатор объекта.

### User

Атрибуты:

- `id`;
- `name`;
- `email`.

Методы:

- `__str__()`;
- `from_data()`;
- `to_data()`.

### Provider

Атрибуты:

- `id`;
- `name`.

Методы:

- `__str__()`;
- `from_data()`;
- `to_data()`.

### Resource

Атрибуты:

- `id`;
- `user` — объект `User`;
- `provider` — объект `Provider`;
- `name`;
- `resource_type`.

Методы:

- `__str__()`;
- `from_data()`;
- `to_data()`.

### Expense

Атрибуты:

- `id`;
- `user` — объект `User`;
- `resource` — объект `Resource`;
- `amount`;
- `date`.

Методы:

- `__str__()`;
- `from_data()`;
- `to_data()`;
- `validate_amount()`.

Сумма хранится в `_amount` и изменяется через свойство `amount`.

## Взаимодействие объектов

`Resource` хранит ссылки на объекты `User` и `Provider`.
`Expense` хранит ссылки на объекты `User` и `Resource`.
После загрузки JSON идентификаторы связываются с созданными объектами.

## Структура

```text
models/
    __init__.py
    entity.py
    user.py
    provider.py
    resource.py
    expense.py
data/
tests/
main.py
users.py
providers.py
resources.py
expenses.py
storage.py
utils.py
```

## Запуск

```text
py -m pip install -r requirements.txt
py main.py
```

## Тесты

```text
py -m pytest -v
```

## Проверка кода

```text
py -m flake8 .
```
