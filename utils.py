from datetime import datetime


def input_int(text: str) -> int:
    while True:
        try:
            return int(input(text))
        except ValueError:
            print("Введите целое число")


def input_float(text: str) -> float:
    while True:
        try:
            value = float(input(text))
            if value < 0:
                raise ValueError
            return value
        except ValueError:
            print("Введите неотрицательное число")


def input_date(text: str) -> str:
    while True:
        value = input(text).strip()
        try:
            date = datetime.strptime(value, "%d.%m.%Y")
            return date.date().isoformat()
        except ValueError:
            print("Введите дату в формате ДД.ММ.ГГГГ")
