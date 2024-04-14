"""Модуль содержит функции с побочными эффектами, которые выводят в консоль информацию"""


def show_start_message() -> None:
    """
    Выводит в консоль информацию о программе
    :return: None
    """
    print("Данная программа реализует операции над матрицами")


def show_continue_message() -> None:
    """
    Выводит в консоль приглашение продолжить
    :return: None
    """
    print("Желаете продолжить? Введите +, если да, иначе что-либо другое:")


def show_finish_message() -> None:
    """
    Выводит в консоль сообщение о завершении работы
    :return: None
    """
    print("Завершение работы")


def show_options_message() -> None:
    """
    Выводит в консоль нумерованный список опций
    :return: None
    """
    print("Выберите опцию из списка (укажите номер 1-7):")
    print("1. Умножение матрицы на число")
    print("2. Транспонирование матрицы")
    print("3. Проверка матрицы на симметричность")
    print("4. Сложение двух матриц")
    print("5. Вычитание двух матриц (из первой матрицы вычитается вторая)")
    print("6. Умножение двух матриц (перед этим будет проверка на возможность умножения")
    print("7. Завершение программы")


def show_option_error_message() -> None:
    '''
    Выводит в консоль сообщение о некорректно введённой опции
    :return: None
    '''
    print("Номер опции введён некорректно: ожидалось число от 1 до 7.")


def show_warning_about_matrix_symmetry_check() -> None:
    """
    Выводит в консоль предупреждение о проверке матрицы на симметричность
    :return: None
    """
    print("Важно: неквадратная матрица всегда будет несимметричной")


def show_warning_about_matrices_addition() -> None:
    """
    Выводит в консоль предупреждение о сложении матриц
    :return: None
    """
    print("Важно: сложение матриц определено только если у них одинаковые размеры")


def show_warning_about_matrices_subtraction() -> None:
    """
    Выводит в консоль предупреждение о вычитании матриц
    :return: None
    """
    print("Важно: вычитание матриц определено только если у них одинаковые размеры")


def show_warning_about_matrices_multiplication() -> None:
    """
    Выводит в консоль предупреждение об умножении матриц
    :return: None
    """
    print("Важно: умножение матриц определено только если количество столбцов первой матрицы равно "
          "количеству строк второй матрицы")


def show_check_symmetry_message(flag_check_symmetry_of_matrix: bool) -> None:
    """
    Выводит в консоль сообщение о проверке матрицы на симметричность
    :param flag_check_symmetry_of_matrix: переменная-флаг: True, если матрица симметричная и False, если нет
    :return: None
    """
    if flag_check_symmetry_of_matrix:
        print("Матрица симметричная")
    else:
        print("Матрица несимметричная")


def show_matrix(rows: int, columns: int, matrix: list[list[int]]) -> None:
    """
    Выводит итоговую матрицу
    :param matrix: матрица
    :return: None
    """
    print(f"Итоговая матрица {rows} x {columns}:")
    for i in range(rows):
        for j in range(columns):
            print(f"{matrix[i][j]:5d}", end="")
        print()
