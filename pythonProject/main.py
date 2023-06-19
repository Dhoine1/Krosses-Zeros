from art import tprint


def menu():   # вывод меню
    tprint("KPECTl/lKl/l \n               - \nHO/ll/lKl/l")
    i = 0
    while (i != 1) and (i != 2):
        print("Что бы начать новую игру наберите 1 \nДля выхода наберите 2")
        i = int(input())
    return i


def pole_art(pole_in):  # вывод на экран поля
    print("+---+---+---+")
    print(f"| {pole_in[1]} | {pole_in[2]} | {pole_in[3]} |")
    print("+---+---+---+")
    print(f"| {pole_in[4]} | {pole_in[5]} | {pole_in[6]} |")
    print("+---+---+---+")
    print(f"| {pole_in[7]} | {pole_in[8]} | {pole_in[9]} |")
    print("+---+---+---+")


def igra(pole_igra):   # сама игра
    count = 1
    pole_art(pole)
    for i in range(9):   # 9 ходов - это максимум
        if count % 2 != 0:   # каждый нечетный ход крестиков, начиная с первого
            print("Ход крестиков")
            a = "X"
            pole_igra = number_cell(pole_igra, a)   # выбор поля для крестиков
            count += 1
            pole_art(pole_igra)
            if test_on_win(pole_igra) == 1:   # проверка победы
                print("ПОБЕДА КРЕСТИКОВ!")
                input()
                break
            elif test_on_win(pole_igra) == 2:
                print("ПОБЕДА НОЛИКОВ!")
                input()
                break
        else:  # каждый четный ход ноликов, начиная со второго
            print("Ход ноликов")
            a = "O"
            pole_igra = number_cell(pole_igra, a)   # выбор поля для ноликов
            count += 1
            pole_art(pole_igra)
            if test_on_win(pole_igra) == 1:  # проверка победы
                print("ПОБЕДА КРЕСТИКОВ!")
                input()
                break
            elif test_on_win(pole_igra) == 2:
                print("ПОБЕДА НОЛИКОВ!")
                input()
                break
        if i == 8:  # если после 9 хода нет победителя, то ничья
            print("НИЧЬЯ. ПОБЕДИЛА ДРУЖБА!")
            input()
            break


def test_on_win(pole_win):   # Проверка победы
    status = 0
    if ((pole_win[1] == "X" and pole_win[2] == "X" and pole_win[3] == "X") or
        (pole_win[4] == "X" and pole_win[5] == "X" and pole_win[6] == "X") or
        (pole_win[7] == "X" and pole_win[8] == "X" and pole_win[9] == "X") or
        (pole_win[1] == "X" and pole_win[4] == "X" and pole_win[7] == "X") or
        (pole_win[2] == "X" and pole_win[5] == "X" and pole_win[8] == "X") or
        (pole_win[3] == "X" and pole_win[6] == "X" and pole_win[9] == "X") or
        (pole_win[1] == "X" and pole_win[5] == "X" and pole_win[9] == "X") or
        (pole_win[3] == "X" and pole_win[5] == "X" and pole_win[7] == "X")):
        status = 1

    elif ((pole_win[1] == "O" and pole_win[2] == "O" and pole_win[3] == "O") or
          (pole_win[4] == "O" and pole_win[5] == "O" and pole_win[6] == "O") or
          (pole_win[7] == "O" and pole_win[8] == "O" and pole_win[9] == "O") or
          (pole_win[1] == "O" and pole_win[4] == "O" and pole_win[7] == "O") or
          (pole_win[2] == "O" and pole_win[5] == "O" and pole_win[8] == "O") or
          (pole_win[3] == "O" and pole_win[6] == "O" and pole_win[9] == "O") or
          (pole_win[1] == "O" and pole_win[5] == "O" and pole_win[9] == "O") or
          (pole_win[3] == "O" and pole_win[5] == "O" and pole_win[7] == "O")):
        status = 2
    return status


def number_cell(pole_cell, a):  # заполнение ячейки поля нужным символом
    hod = int(input("Введите номер поля: "))
    while hod <= 0 or hod >= 10 or pole_cell[hod] == "X" or pole_cell[hod] == "O":  # проверка корректности ввода
        hod = int(input("Введите номер поля: "))                                    # и того, что ячейка свободна
    pole_cell[hod] = a
    return pole_cell


while 1:     # сама программа игры
    change = menu()
    if change == 1:  # 1-игра
        pole = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}   # стартовое поле
        igra(pole)
    elif change == 2:  # 2-выход
        break
