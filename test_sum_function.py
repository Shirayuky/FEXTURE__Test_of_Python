import pytest
from sum_function import sum_func

# делаем фикстуры для чисел

@pytest.fixture()
def get_positive_numbers():
    return [1, 1]

@pytest.fixture()
def get_negative_numbers():
    return [-10, -30]

@pytest.fixture()
def get_positive_and_negative_numbers():
    return [1, -1]

# Tests
class TestSunFunc:
    # Передаем в аргумент вьюшку
    def test_sum_positive(self, get_positive_numbers):
        # Обращаемся по индексу
        c = sum_func(get_positive_numbers[0], get_positive_numbers[1])
        assert c > 0, "Ошибка: сумма чисел не положительная"
        assert c == 2, "Ошибка в сложении положительных чисел"

    def test_sum_negative(self, get_negative_numbers):
        # Обращаемся по индексу
        c = sum_func(get_negative_numbers[0], get_negative_numbers[1])
        assert c < 0, "Ошибка: сумма чисел не отрицательная"
        assert c == -40, "Ошибка в сложении положительных чисел"

    def test_sum_positive_and_negative(self, get_positive_and_negative_numbers):
        # Обращаемся по индексу
        c = sum_func(get_positive_and_negative_numbers[0], get_positive_and_negative_numbers[1])
        assert c == 0, "Ошибка: сумма чисел не равна 0"


