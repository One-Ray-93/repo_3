import math, random

def test_greeting():
    name = "Анна"
    age = 25
    hi = "Привет"
    a = "Тебе"
    b = "! "
    c = "лет"

    output = f"{hi}, {name}{b}{a} {age} {c}."
    assert output == "Привет, Анна! Тебе 25 лет."


def test_rectangle():

    a = 10
    b = 20

    perimeter = (a + b) * 2
    assert perimeter == 60

    area = (a * b)
    assert area == 200


def test_circle():
    r = 23

    area = math.pi * r **2
    assert area == 1661.9025137490005

    length = 2 * math.pi * r
    assert length == 144.51326206513048

    print(area, length)


def test_random_list():
    l = [random.randint(1, 100) for _ in range(10)]
    l.sort()

    assert len(l) == 10
    assert all(l[i] <= l[i + 1] for i in range(len(l) - 1))



def test_unique_elements():

    l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]
    l = list(set(l))

    assert isinstance(l, list)
    assert len(l) == 10
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_dicts():
    """
    Создайте словарь из двух списков.
    Используйте первый список как ключи, а второй - как значения.
    Подсказка: используйте встроенную функцию zip.
    """
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]

    d = {}

    assert isinstance(d, dict)
    assert len(d) == 5
    assert list(d.keys()) == first
    assert list(d.values()) == second