"""Модуль содержит функции с побочными эффектами, которые запрашивают и считывают из консоли данные от пользователя"""


def get_answer() -> str:
    """
    Запрашивает и считывает из консоли ответ пользователя
    :return: ответ пользователя answer
    """
    answer = input()
    return answer


def get_matrix_size(number_of_matrix_size: int = 0) -> tuple[int, int]:
    """
    Запрашивает и считывает из консоли размеры матрицы
    :param number_of_matrix_size: номер размеров матрицы; если для опции нужно ввести только одну матрицу,
    то по умолчанию 0;
    иначе если нужно две матрицы, то передаём либо 1, либо 2 в зависимости от того,
    для какой по счёту матрицы вводим размеры;
    нужен для того, чтобы в приглашении ко входу было написано, для какой именно матрицы вводим размеры,
    для первой или второй
    :return: количество строк rows и количество столбцов columns
    """
    if number_of_matrix_size == 0:
        print("Введите размеры матрицы (хотя бы 1 строка и хотя бы 1 столбец):")
    else:
        text = "первой" if number_of_matrix_size == 1 else "второй"
        print(f"Введите размеры {text} матрицы (хотя бы 1 строка и хотя бы 1 столбец):")
    rows = int(input("Количество строк: "))
    columns = int(input("Количество столбцов: "))
    return rows, columns


def get_matrix(rows: int, columns: int, number_of_matrix: int = 0) -> list[list[int]]:
    """
    Запрашивает и считывает из консоли матрицу, соответствующую ранее введенным размерам rows и columns
    :param rows: количество строк
    :param columns: количество столбцов
    :param number_of_matrix: номер матрицы; если для опции нужно ввести только одну матрицу, то по умолчанию 0;
    иначе если нужно две матрицы, то передаём либо 1, либо 2 в зависимости от того, какую по счёту матрицу вводим;
    нужен для того, чтобы в приглашении ко входу было написано, какую именно матрицу вводим, первую или вторую
    :return: матрица matrix
    """
    if number_of_matrix == 0:
        print(f"Введите матрицу {rows} x {columns}:")
    else:
        text = "первую" if number_of_matrix == 1 else "вторую"
        print(f"Введите {text} матрицу {rows} x {columns}:")
    matrix = []
    for i in range(rows):
        tmp_row = [int(x) for x in input().split()]
        matrix.append(tmp_row)
    return matrix


def get_number() -> int:
    """
    Запрашивает и считывает из консоли число
    :return: число number
    """
    number = int(input("Введите число: "))
    return number
