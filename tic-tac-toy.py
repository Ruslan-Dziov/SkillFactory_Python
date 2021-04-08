# Layout
a = '_'
b = '_'
c = '_'
d = '_'
e = '_'
f = '_'
j = ' '
k = ' '
l = ' '
print("""
    Правила игры
Чтобы сделать ход, необходимо указать две цифры через пробел,
которые определят место в матрице, первая цифра это ось Х, вторая - Y

         0 1 2

    0    {}|{}|{}
    1    {}|{}|{}
    2    {}|{}|{}
    """.format(a, b, c, d, e, f, j, k, l))
# Переменные и списки
player1 = None
player2 = None
step_pl1 = None
step_pl2 = None
list_of_moves1 = []
list_of_moves2 = []
list_to_win1 = []
list_to_win2 = []
winner = 0
# Варианты выигрыша
wins = [[(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)], [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)], [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]]
# определяем кто первым ходит, запускаем цикл игры
import random

step1 = random.randint(1, 2)
while winner == 0:
    if step1 % 2 == 0:
        player1 = 1
        player2 = 0
    else:
        palyer2 = 1
        player1 = 0
    step1 += 1
    if player1 == 1:
        step_pl1 = input('Игрок 1 ходит, введите X и Y через пробел ')
        step_pl1 = list(step_pl1.split())
        step_pl1 = tuple(map(int, step_pl1))
        while (step_pl1 in list_of_moves1) or (step_pl1 in list_of_moves2):
            print('Такой ход уже сделали')
            step_pl1 = input('Игрок 1 ходит, введите X и Y через пробел ')
            step_pl1 = list(step_pl1.split())
            step_pl1 = tuple(map(int, step_pl1))
        if step_pl1 == (0, 0):
            a = 'X'
        elif step_pl1 == (0, 1):
            b = 'X'
        elif step_pl1 == (0, 2):
            c = 'X'
        elif step_pl1 == (1, 0):
            d = 'X'
        elif step_pl1 == (1, 1):
            e = 'X'
        elif step_pl1 == (1, 2):
            f = 'X'
        elif step_pl1 == (2, 0):
            j = 'X'
        elif step_pl1 == (2, 1):
            k = 'X'
        elif step_pl1 == (2, 2):
            l = 'X'
        list_of_moves1.append(step_pl1)
        for win in wins:
            for w in win:
                if w in list_of_moves1:
                    list_to_win1.append(True)
                else:
                    list_to_win1.append(False)
            if list_to_win1[0] and list_to_win1[1] and list_to_win1[2] == True:
                print('*' * 30, '\nВыиграл игрок 1!')
                winner = 1
                break
            else:
                list_to_win1 = []
    else:
        step_pl2 = input('Игрок 2 ходит, введите X и Y через пробел ')
        step_pl2 = list(step_pl2.split())
        step_pl2 = tuple(map(int, step_pl2))
        while (step_pl2 in list_of_moves1) or (step_pl2 in list_of_moves2):
            print('Такой ход уже сделали')
            step_pl2 = input('Игрок 2 ходит, введите X и Y через пробел ')
            step_pl2 = list(step_pl2.split())
            step_pl2 = tuple(map(int, step_pl2))
        if step_pl2 == (0, 0):
            a = '0'
        elif step_pl2 == (0, 1):
            b = '0'
        elif step_pl2 == (0, 2):
            c = '0'
        elif step_pl2 == (1, 0):
            d = '0'
        elif step_pl2 == (1, 1):
            e = '0'
        elif step_pl2 == (1, 2):
            f = '0'
        elif step_pl2 == (2, 0):
            j = '0'
        elif step_pl2 == (2, 1):
            k = '0'
        elif step_pl2 == (2, 2):
            l = '0'
        list_of_moves2.append(step_pl2)
        for win in wins:
            for w in win:
                if w in list_of_moves2:
                    list_to_win2.append(True)
                else:
                    list_to_win2.append(False)
            if list_to_win2[0] and list_to_win2[1] and list_to_win2[2] == True:
                print('*' * 30, '\nВыиграл игрок 2!')
                winner = 1
                break
            else:
                list_to_win2 = []
    print("""

         0 1 2

    0    {}|{}|{}
    1    {}|{}|{}
    2    {}|{}|{}
    """.format(a, b, c, d, e, f, j, k, l))
