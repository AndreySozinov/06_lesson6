# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# 📌 Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# 📌 Для простоты договоримся, что год может быть в диапазоне # [1, 9999].
# 📌 Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# 📌 Проверку года на високосность вынести в отдельную защищённую функцию.

# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
from sys import argv

__all__ = ['check_exist']


def check_exist(input_date: str) -> bool:
    numbers = list(map(int, input_date.split('.')))
    day, month, year = numbers

    if 1 <= year <= 9999 or 1 <= month <= 12 or 1 <= day <= 31:
        match month:
            case 4 | 6 | 9 | 11:
                if day == 31:
                    return False
            case 2:
                if day == 29 and not _leap_year(year) or day > 29:
                    return False
                return True
            case _:
                return True
    return False


def _leap_year(year: int) -> bool:
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


if __name__ == '__main__':
    # print(f'01.01.0001 {check_exist("01.01.0001")}')
    # print(f'29.02.2022 {check_exist("29.02.2022")}')
    # print(f'29.02.2020 {check_exist("29.02.2020")}')
    # print(f'31.02.1977 {check_exist("31.02.1977")}')

    '''Ожидаем передачи одного аргумента - строки формата DD.MM.YYYY'''
    name, arg = argv
    print(check_exist(arg))
