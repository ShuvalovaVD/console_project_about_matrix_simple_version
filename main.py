"""
Консольный проект, реализующий операции над матрицами.

Минус данной программы в том, что здесь нет отлова ошибок ввода. То есть пользователь может ввести вместо числа
строку, и тогда всё сломается. Но работа с ошибками и исключениями усложнила бы программу.
"""

def get_one_matrix():
    """Получает матрицу от пользователя."""
    print("Введите размеры матрицы:")
    rows = int(input("Количество строк: "))
    columns = int(input("Количество столбцов: "))
    print(f"Введите матрицу {rows} x {columns}:")
    matrix = [[int(el) for el in input().split()] for i in range(rows)]
    return rows, columns, matrix


def get_two_matrices():
    """Получает две матрицы от пользователя."""
    print("Введите размеры первой матрицы:")
    rows_1 = int(input("Количество строк: "))
    columns_1 = int(input("Количество столбцов: "))
    print(f"Введите первую матрицу {rows_1} x {columns_1}:")
    matrix_1 = [[int(el) for el in input().split()] for i in range(rows_1)]
    print("Введите размеры второй матрицы:")
    rows_2 = int(input("Количество строк: "))
    columns_2 = int(input("Количество столбцов: "))
    print(f"Введите вторую матрицу {rows_2} x {columns_2}:")
    matrix_2 = [[int(el) for el in input().split()] for i in range(rows_2)]
    return rows_1, columns_1, matrix_1, rows_2, columns_2, matrix_2


def show_matrix_result(rows_result, columns_result, matrix_result):
    """Выводит итоговую матрицу пользователю."""
    print(f"Итоговая матрица {rows_result} x {columns_result}:")
    for i in range(rows_result):
        for j in range(columns_result):
            print(f"{matrix_result[i][j]:5d}", end="")
        print()


def multiply_matrix_by_number(rows, columns, matrix, number):
    """Умножает матрицу на число."""
    matrix_result = [[matrix[i][j] * number for j in range(columns)] for i in range(rows)]
    return matrix_result


def transpose_matrix(rows, columns, matrix):
    """Транспонирует матрицу."""
    matrix_result = [[matrix[i][j] for i in range(rows)] for j in range(columns)]
    return matrix_result


def check_symmetry_of_matrix(rows, columns, matrix):
    """
    Проверяет матрицу на симметричность и возвращает результат типа bool:
    True - если матрица симметрична, False - если матрица несимметрична.
    """
    if rows != columns:  # если она неквадратная, сразу понятно, что она несимметричная
        return False
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] != matrix[j][i]:  # если встретили хотя бы одну асимметрию, возвращаем False
                return False
    return True  # иначе если не встретилось асимметрий, возвращаем True


def add_two_matrices(rows, columns, matrix_1, matrix_2):
    """
    Складывает две матрицы. Предполагается, что размеры у матриц одинаковые: только тогда сложение матриц определено.
    """
    matrix_result = [[matrix_1[i][j] + matrix_2[i][j] for j in range(columns)] for i in range(rows)]
    return matrix_result


def subtract_two_matrices(rows, columns, matrix_1, matrix_2):
    """
    Вычитает из первой матрицы вторую. Использует интересный подход к решению: вычесть из первой матрицы вторую - это
    то же самое, что вторую матрицу умножить на (-1) и прибавить к первой матрице:
    matrix_1 - matrix_2 = matrix_1 + (-1 * matrix_2)
    Предполагается, что размеры у матриц одинаковые: только тогда вычитание матриц определено.
    """
    matrix_2_new = multiply_matrix_by_number(rows, columns, matrix_2, -1)
    matrix_result = add_two_matrices(rows, columns, matrix_1, matrix_2_new)
    return matrix_result


def multiply_two_matrices(rows_1, columns_1, matrix_1, rows_2, columns_2, matrix_2):
    """
    Умножает первую матрицу на вторую. Предполагается, что количество столбцов первой матрицы равно числу строк
    второй матрицы: только тогда умножение первой матрицы на вторую матрицу определено.
    """
    rows_result, columns_result = rows_1, columns_2
    # при умножении первой матрицы на вторую матрицу итоговая матрица будет иметь размеры rows_1 x columns_2
    matrix_result = [[0 for j in range(columns_2)] for i in range(rows_1)]  # изначально заполняем нулями
    for i in range(rows_1):
        for j in range(columns_2):
            matrix_result[i][j] = sum([matrix_1[i][k] * matrix_2[k][j] for k in range(columns_1)])
    return matrix_result


def main():
    """Главная функция программы, вызывает другие функции из других модулей."""
    print("Данная программа реализует операции над матрицами")  # стартовое сообщение выведем один раз
    while True:  # программа будет работать много раз, до тех пор, пока пользователь не выберет опцию "выход"
        # программма реализует много действий, предлагаем пользователю выбрать одну опцию
        print("Выберите опцию из списка (укажите номер 1-7):")
        print("1. Умножение матрицы на число")
        print("2. Транспонирование матрицы")
        print("3. Проверка матрицы на симметричность")
        print("4. Сложение двух матриц")
        print("5. Вычитание двух матриц (из первой матрицы вычитается вторая)")
        print("6. Умножение двух матриц")
        print("7. Завершение программы")
        answer = input()  # получаем ответ от пользователя
        if answer == "1":
            rows, columns, matrix = get_one_matrix()
            number = int(input("Введите целое число: "))
            rows_result, columns_result = rows, columns
            matrix_result = multiply_matrix_by_number(rows, columns, matrix, number)
            show_matrix_result(rows_result, columns_result, matrix_result)
        elif answer == "2":
            rows, columns, matrix = get_one_matrix()
            rows_result, columns_result = columns, rows  # у транспонированной матрицы поменяются размеры наоборот
            matrix_result = transpose_matrix(rows, columns, matrix)
            show_matrix_result(rows_result, columns_result, matrix_result)
        elif answer == "3":
            rows, columns, matrix = get_one_matrix()
            flag_result = check_symmetry_of_matrix(rows, columns, matrix)
            # flag_result - переменная-флаг: True, если матрица симметричная и False, если нет
            if flag_result:  # if flag_result == True:
                print("Матрица симметричная")
            else:
                print("Матрица несимметричная")
        elif answer == "4":
            rows_1, columns_1, matrix_1, rows_2, columns_2, matrix_2 = get_two_matrices()
            # предполагается, что размеры у матриц одинаковые: только тогда сложение матриц определено
            rows_result, columns_result = rows_1, columns_1
            matrix_result = add_two_matrices(rows_result, columns_result, matrix_1, matrix_2)
            show_matrix_result(rows_result, columns_result, matrix_result)
        elif answer == "5":
            rows_1, columns_1, matrix_1, rows_2, columns_2, matrix_2 = get_two_matrices()
            # предполагается, что размеры у матриц одинаковые: только тогда вычитание матриц определено
            rows_result, columns_result = rows_1, columns_1
            matrix_result = subtract_two_matrices(rows_result, columns_result, matrix_1, matrix_2)
            show_matrix_result(rows_result, columns_result, matrix_result)
        elif answer == "6":
            rows_1, columns_1, matrix_1, rows_2, columns_2, matrix_2 = get_two_matrices()
            # предполагается, что количество столбцов первой матрицы равно числу строк второй матрицы:
            # только тогда умножение первой матрицы на вторую матрицу определено
            rows_result, columns_result = rows_1, columns_2
            # при умножении первой матрицы на вторую матрицу итоговая матрица будет иметь размеры rows_1 x columns_2
            matrix_result = multiply_two_matrices(rows_1, columns_1, matrix_1, rows_2, columns_2, matrix_2)
            show_matrix_result(rows_result, columns_result, matrix_result)
        elif answer == "7":
            break  # выход из вечного цикла
        print("Желаете продолжить? Введите +, если да, иначе что-либо другое:")  # сообщение о продолжении работы
        answer = input()  # получаем ответ от пользователя
        if answer != "+":
            break  # выход из вечного цикла
    print("Завершение работы")  # сообщение о завершении работы программы по завершению цикла


main()  # вызываем главную функцию
