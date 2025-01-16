from lib import count_common_elements

def test_count_common_elements():
    # Тест 1: Одинаковые элементы в двух списках
    list1 = [1, 2, 3, 4]
    list2 = [2, 3, 4, 5]
    assert count_common_elements(list1, list2) == 3, "Тест 1 не пройден"

    # Тест 2: Одинаковые элементы в трех списках
    list3 = [3, 4, 5, 6]
    assert count_common_elements(list1, list2, list3) == 2, "Тест 2 не пройден"

    # Тест 3: Нет одинаковых элементов
    list4 = [7, 8, 9]
    assert count_common_elements(list1, list4) == 0, "Тест 3 не пройден"

    # Тест 4: Пустые списки
    assert count_common_elements([], []) == 0, "Тест 4 не пройден"

    print("Все тесты пройдены успешно!")

if __name__ == "__main__":
    test_count_common_elements()