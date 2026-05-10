import random

def input_elems():
    """
    Функция для ручного ввода элементов списка.
    :return: Список элементов, заданных пользователем.
    """
    while True:
        try:
            elems = list(map(int, input("Введите значения списка через пробел: ").split()))
            return elems
        except ValueError:
            print("Возникла ошибка, попробуйте заново.")

def random_elems():
    """
    Функция, генерирующая случайные элементы для списка в заданном диапазоне.
    :return: Список случайных элементов.
    """
    size_elems = int(input("Сколько элементов должно быть в списке: "))
    start_el = int(input("Введите начальный диапазон: "))
    stop_el = int(input("Введите конечный диапазон: "))
    elems = [random.randint(start_el, stop_el) for _ in range(size_elems)]
    return elems

def merge_sort(arr):
    """
    Реализация сортировки слиянием (ручная).
    :param arr: Исходный список.
    :return: Новый отсортированный список.
    """
    if len(arr) <= 1:
        return arr[:]

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def sort_standard(elems):
    """
    Сортировка с использованием встроенной функции sorted().
    :param elems: Исходный список.
    :return: Новый отсортированный список.
    """
    return sorted(elems)

def sort_merge_manual(elems):
    """
    Сортировка с использованием ручной реализации слиянием.
    :param elems: Исходный список.
    :return: Новый отсортированный список.
    """
    return merge_sort(elems)

# Основная часть
while True:
    try:
        choice = int(
            input(
                "Задать элементы вручную [1] или с помощью автоматической генерации [2]. Введите [1/2] соответственно: "))
        if choice in [1, 2]:
            break
        print("Неверно введено значение, повторите попытку.")
    except ValueError:
        print("Неверно введено значение, повторите попытку.")

if choice == 1:
    elems = input_elems()
elif choice == 2:
    elems = random_elems()
    print("Исходный список:", *elems)

while True:
    try:
        choice2 = int(
            input(
                "Вывести отсортированный список используя стандартные функции python [1] или ручную сортировку слиянием [2]. Введите [1/2] соответственно: "))
        if choice2 in [1, 2]:
            break
        print("Неверно введено значение, повторите попытку.")
    except ValueError:
        print("Неверно введено значение, повторите попытку.")

if choice2 == 1:
    result = sort_standard(elems)
elif choice2 == 2:
    result = sort_merge_manual(elems)

if not result:
    print("Список пуст.")
else:
    print("Отсортированный список:", *result)