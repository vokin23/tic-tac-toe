import time

print(" Игра Крестики-нолики ")

first_player = input("Введите фамилию, имя и отчество первого игрока: ").split()
second_player = input("Введите фамилию, имя и отчество второго игрока: ").split()
first_player.pop(0)
second_player.pop(0)
time.sleep(1)
print()
print(*first_player, ", для совершения хода выберете символи введите его:", end=" ")
char1 = input()
print(*second_player, ", для совершения хода выберете символи введите его:", end=" ")
char2 = input()
s = char1 + char2
time.sleep(1)

board = list(i for i in range(1,10))


def draw_board():
    '''Функция для рисования игрового поля в консоле'''
    print("-" * 13)
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-" * 13)

def game_step(index, char):
    if index > 9 or index < 1 or (str(board[index - 1]) in s):
        return False
    board[index - 1] = char
    return True


def cheak_win():
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    win = False

    for kek in win_coord:
        if board[kek[0]] == board[kek[1]] == board[kek[2]]:
            win = board[kek[0]]

    return win

def main():
    current_player = char1
    step = 1
    draw_board()

    while (step < 10) and (cheak_win() == False):
        index = input("Ход игрока " + current_player + ". Введите номер поля: ")
        try:
            kuk = int(index)
            if game_step(kuk, current_player):
                print("Хороший ход!")

                if (current_player == char1):
                    current_player = char2
                else:
                    current_player = char1

                draw_board()
                step += 1
            else:
                print("Упс, что-то пошло не так! Повторите ход!")
        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue

    if step != 10:
        print("Победа игрока: ", cheak_win())
    else:
        print("Победила дружба")

main()
