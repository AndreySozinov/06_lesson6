# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код,
# решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

# 📌 Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для
# случайной расстановки ферзей в задаче выше. Проверяйте различный случайные варианты и
# выведите 4 успешных расстановки.
from random import randint as r
BOARD_SIZE = 8


def eight_queens_check(coordinates: [[int]]) -> bool:
    """Проверка расстановки 8 ферзей"""
    # Подготовка доски
    chess_board = [[0 for j in range(BOARD_SIZE)] for i in range(BOARD_SIZE)]

    #Расстановка ферзей
    for queen in coordinates:
        chess_board[queen[0]-1][queen[1]-1] = 1

    # Проверка горизонталей и вертикалей
    for i in range(BOARD_SIZE):
        summa = 0
        summa1 = 0
        for j in range(BOARD_SIZE):
            summa += chess_board[i][j]
            summa1 += chess_board[j][i]
        if summa > 1 or summa1 > 1:
            return False

    # Проверка диагоналей
    for i in range(2, BOARD_SIZE+1):
        summa = 0
        for j in range(i):
            summa += chess_board[j][i-j-1]
        if summa > 1:
            return False
    for i in range(2, BOARD_SIZE):
        summa = 0
        for j in range(i):
            summa += chess_board[BOARD_SIZE-i+j][BOARD_SIZE-j-1]
        if summa > 1:
            return False
    for i in range(BOARD_SIZE+1):
        summa = 0
        for j in range(i):
            summa += chess_board[j][j+BOARD_SIZE-i]
        if summa > 1:
            return False
    for i in range(BOARD_SIZE-1):
        summa = 0
        for j in range(i+1):
            summa += chess_board[BOARD_SIZE-i-1+j][j]
        if summa > 1:
            return False
    return True


def arrangement():
    i = 0
    while i < 4:
        queens_coor = [[r(1, 8) for j in range(2)] for i in range(BOARD_SIZE)]
        if eight_queens_check(queens_coor):
            print(queens_coor)
            print_chessboard(queens_coor)
            i += 1


def print_chessboard(coordinates: [[int]]):
    # Подготовка доски
    chess_board = [[0 for j in range(BOARD_SIZE)] for i in range(BOARD_SIZE)]

    # Расстановка ферзей
    for queen in coordinates:
        chess_board[queen[0] - 1][queen[1] - 1] = 1

    # Вывод доски на печать
    print(' - - - - - - - -')
    for i in range(len(chess_board)):
        for j in range(len(chess_board[0])):
            if chess_board[i][j] == 1:
                print(' Ф ', end=' ')
            else:
                print('   ', end=' ')
        print()


if __name__ == '__main__':
    arrangement()
