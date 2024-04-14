"""Модуль содержит функции без побочных эффектов, реализующие логические операции над матрицами"""


def multiply_matrix_by_number(rows: int, columns: int, matrix: list[list[int]], number: int) -> list[list[int]]:
    """
    Умножает матрицу на число
    :param rows: количество строк
    :param columns: количество столбцов
    :param matrix: матрица
    :param number: число
    :return: матрица matrix, умноженная на число
    """
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] *= number
    return matrix


def transpose_matrix(rows: int, columns: int, matrix: list[list[int]]) -> list[list[int]]:
    """
    Транспонирует матрицу
    :param rows: количество строк
    :param columns: количество столбцов
    :param matrix: матрица
    :return: транспонированная матрица matrix_result
    """
    rows_result, columns_result = columns, rows  # у транспонированной матрицы поменяются размеры наоборот
    matrix_result = []
    # изначально заполним её нулями
    for i in range(rows_result):
        tmp_row = [0] * columns_result
        matrix_result.append(tmp_row)
    # теперь перезапишем
    for i in range(rows_result):
        for j in range(columns_result):
            matrix_result[i][j] = matrix[j][i]
    return matrix_result


def check_symmetry_of_matrix(rows: int, columns: int, matrix: list[list[int]]) -> bool:
    """
    Проверяет матрицу на симметричность
    :param rows: количество строк
    :param columns: количество столбцов
    :param matrix: матрица
    :return: True или False, если матрица симметричная и несимметричная соответственно
    """
    if rows != columns:  # если она неквадратная, сразу понятно, что она несимметричная
        return False
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] != matrix[j][i]:  # если встретили хотя бы одну асимметрию, возвращаем False
                return False
    return True  # иначе если не встретилось асимметрий, возвращаем True


def add_two_matrices(rows: int, columns: int, matrix_1: list[list[int]], matrix_2: list[list[int]]) -> list[list[int]]:
    """
    Складывает две матрицы, результат сохраняется в матрицу matrix_1, предполагается, что размеры у матриц одинаковые
    :param rows: количество строк у двух матриц
    :param columns: количество столбцов у двух матриц
    :param matrix_1: первая матрица
    :param matrix_2: вторая матрица
    :return: результирующая матрица matrix_1
    """
    for i in range(rows):
        for j in range(columns):
            matrix_1[i][j] += matrix_2[i][j]
    return matrix_1


def subtract_two_matrices(rows: int, columns: int, matrix_1: list[list[int]],
                          matrix_2: list[list[int]])-> list[list[int]]:
    """
    Вычитает из первой матрицы вторую, результат сохраняется в матрицу matrix_1,
    предполагается, что размеры у матриц одинаковые
    :param rows: количество строк
    :param columns: количество столбцов
    :param matrix_1: первая матрица
    :param matrix_2: вторая матрица
    :return: результирующая матрица matrix_1
    """
    # matrix_1 - matrix_2 = matrix_1 + (-1 * matrix_2)
    matrix_2 = multiply_matrix_by_number(rows, columns, matrix_2, -1)
    matrix_1 = add_two_matrices(rows, columns, matrix_1, matrix_2)
    return matrix_1


def multiply_two_matrices(rows_1: int, columns_1: int, matrix_1: list[list[int]],
                          rows_2: int, columns_2: int, matrix_2: list[list[int]]) -> list[list[int]]:
    """
    Умножает две матрицы, предполагается что количество столбцов первой матрицы columns_1
    равно количеству строк второй матрицы rows_2
    :param rows_1: количество строк первой матрицы
    :param columns_1: количество столбцов первой матрицы
    :param matrix_1: первая матрица
    :param rows_2: количество строк второй матрицы
    :param columns_2: количество столбцов второй матрицы
    :param matrix_2: вторая матрица
    :return: результирующая матрица matrix_result
    """
    # при умножении двух матриц итоговая матрица будет иметь размеры rows_1 x columns_2
    rows_result, columns_result = rows_1, columns_2
    matrix_result = []
    # изначально заполним её нулями
    for i in range(rows_result):
        tmp_row = [0] * columns_result
        matrix_result.append(tmp_row)
    # теперь перезапишем
    for i in range(rows_result):
        for j in range(columns_result):
            # ячейка [i][j] matrix_result - это i-ая строка matrix_1, умноженная покоординатно на j-ый столбец matrix_2
            for k in range(columns_1):  # или rows2, неважно, они равны, если умножение матриц определено
                matrix_result[i][j] += matrix_1[i][k] * matrix_2[k][j]  # постепенно покоординатно умножаем
    return matrix_result
