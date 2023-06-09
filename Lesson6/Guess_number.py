# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

# Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
# Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# Для преобразования строковых аргументов командной строки в числовые параметры
# используйте генераторное выражение.
from random import randint
from sys import argv


def guess(start: int, end: int = 100, tries: int = 10) -> bool:
    goal = randint(start, end+1)

    for i in range(tries):
        attempt = int(input('Угадай число: '))
        if goal < attempt:
            print('Меньше')
        elif goal > attempt:
            print('Больше')
        else:
            print('Угадал!')
            return True
    print('Попытки закончились')
    return False


if __name__ == '__main__':
    name, *arg = argv
    print(guess(*(int(x) for x in arg)))

__all__ = ['guess']
