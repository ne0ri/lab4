import numpy as np


def generate_matrix():

    while True:
        try:
            n = int(input("Введите размер квадратной матрицы N: "))
            if n > 0:
                break
            else:
                print("Размер матрицы должен быть положительным числом.")
        except ValueError:
            print("Неверно введены значения. Попробуйте еще раз.")

    while True:
        try:
            start_el = int(input("Введите начальное значение диапазона: "))
            stop_el = int(input("Введите конечное значение диапазона: "))
            if stop_el >= start_el:
                break
            else:
                print("Конечное значение должно быть не меньше начального.")
        except ValueError:
            print("Неверно введены значения. Попробуйте еще раз.")

    matrix = np.random.randint(start_el, stop_el + 1, size=(n, n))
    return matrix, n


def process_matrix(matrix, n):

    result = matrix.copy().astype(float)
    for i in range(n):
        for j in range(i + 1, n):
            avg = (result[i, j] + result[j, i]) / 2.0
            result[i, j] = avg
            result[j, i] = avg
    return result


matrix, n = generate_matrix()
processed = process_matrix(matrix, n)

with open("output.txt", "w", encoding="UTF-8") as f:
    f.write("Исходная матрица:\n")
    np.savetxt(f, matrix, fmt="%d")
    f.write("\nОбработанная матрица (полусуммы симметричных элементов):\n")
    np.savetxt(f, processed, fmt="%.2f")

print("Исходная матрица:")
print(matrix)
print("\nОбработанная матрица:")
print(processed)
print("\nРезультат сохранён в файл output.txt")