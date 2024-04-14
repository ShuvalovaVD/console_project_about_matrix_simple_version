"""
Главный модуль программы: с него начинается запуск программы и в него импортируются другие модули.
Здесь находится функция main(), которая вызывает функции из других модулей.

Минус данной программы в том, что здесь нет отлова ошибок ввода. То есть пользователь может ввести вместо числа строку,
и тогда всё сломается. Но работа с ошибками и исключениями значительно бы усложнила программу.
"""

# импортируем наши вспомогательные модули
import console_input
import console_output
import logic


def main() -> None:
    """
    Главная функция программы, вызывает другие функции из других модулей
    :return: None
    """
    console_output.show_start_message()  # стартовое сообщение выведем один раз
    while True:  # программа будет работать много раз, до тех пор, пока пользователь не выберет опцию "выход"
        # программма реализует много действий, предлагаем пользователю выбрать одну опцию
        console_output.show_options_message()
        answer = console_input.get_answer()  # получаем ответ от пользователя
        if answer == "1":
            rows, columns = console_input.get_matrix_size()
            matrix = console_input.get_matrix(rows, columns)
            number = console_input.get_number()
            matrix_result = logic.multiply_matrix_by_number(rows, columns, matrix, number)
            console_output.show_matrix(rows, columns, matrix_result)
        elif answer == "2":
            rows, columns = console_input.get_matrix_size()
            matrix = console_input.get_matrix(rows, columns)
            rows_result, columns_result = columns, rows
            # у транспонированной матрицы поменяются размеры наоборот
            matrix_result = logic.transpose_matrix(rows, columns, matrix)
            console_output.show_matrix(rows_result, columns_result, matrix_result)
        elif answer == "3":
            console_output.show_warning_about_matrix_symmetry_check()
            rows, columns = console_input.get_matrix_size()
            matrix = console_input.get_matrix(rows, columns)
            # переменная-флаг: True, если матрица симметричная и False, если нет
            flag_check_symmetry_of_matrix = logic.check_symmetry_of_matrix(rows, columns, matrix)
            console_output.show_check_symmetry_message(flag_check_symmetry_of_matrix)
        elif answer == "4":
            console_output.show_warning_about_matrices_addition()
            # с помощью параметра number_of_matrix_size указываем, что будет ввод именно первой матрицы
            rows_1, columns_1 = console_input.get_matrix_size(number_of_matrix_size=1)
            matrix_1 = console_input.get_matrix(rows_1, columns_1, number_of_matrix=1)
            # с помощью параметра number_of_matrix_size указываем, что будет ввод именно второй матрицы
            rows_2, columns_2 = console_input.get_matrix_size(number_of_matrix_size=2)
            matrix_2 = console_input.get_matrix(rows_2, columns_2, number_of_matrix=2)
            rows, columns = rows_1, columns_1  # предполагается, что размеры у матриц одинаковые
            matrix_result = logic.add_two_matrices(rows, columns, matrix_1, matrix_2)
            console_output.show_matrix(rows, columns, matrix_result)
        elif answer == "5":
            console_output.show_warning_about_matrices_subtraction()
            # с помощью параметра number_of_matrix_size указываем, что будет ввод именно первой матрицы
            rows_1, columns_1 = console_input.get_matrix_size(number_of_matrix_size=1)
            matrix_1 = console_input.get_matrix(rows_1, columns_1, number_of_matrix=1)
            # с помощью параметра number_of_matrix_size указываем, что будет ввод именно второй матрицы
            rows_2, columns_2 = console_input.get_matrix_size(number_of_matrix_size=2)
            matrix_2 = console_input.get_matrix(rows_2, columns_2, number_of_matrix=2)
            rows, columns = rows_1, columns_1  # предполагается, что размеры у матриц одинаковые
            matrix_result = logic.subtract_two_matrices(rows, columns, matrix_1, matrix_2)
            console_output.show_matrix(rows, columns, matrix_result)
        elif answer == "6":
            console_output.show_warning_about_matrices_multiplication()
            # с помощью параметра number_of_matrix_size указываем, что будет ввод именно первой матрицы
            rows_1, columns_1 = console_input.get_matrix_size(number_of_matrix_size=1)
            matrix_1 = console_input.get_matrix(rows_1, columns_1, number_of_matrix=1)
            # с помощью параметра number_of_matrix_size указываем, что будет ввод именно второй матрицы
            rows_2, columns_2 = console_input.get_matrix_size(number_of_matrix_size=2)
            matrix_2 = console_input.get_matrix(rows_2, columns_2, number_of_matrix=2)
            # предполагается, что количество столбцов первой матрицы равно числу строк второй матрицы
            # при умножении двух матриц итоговая матрица будет иметь размеры rows_1 x columns_2
            rows, columns = rows_1, columns_2
            matrix_result = logic.multiply_two_matrices(rows_1, columns_1, matrix_1, rows_2, columns_2, matrix_2)
            console_output.show_matrix(rows, columns, matrix_result)
        elif answer == "7":
            break  # выход из вечного цикла
        else:
            console_output.show_option_error_message()  # сообщение об ошибке
        console_output.show_continue_message()  # сообщение о продолжении или прекращении работы
        answer = console_input.get_answer()  # получаем ответ от пользователя
        if answer != "+":
            break  # выход из вечного цикла
    console_output.show_finish_message()  # сообщение о завершении работы программы по завершению цикла


# модуль main.py главный: с него начинается запуск программы и в него импортируются другие модули
if __name__ == '__main__':
    main()
