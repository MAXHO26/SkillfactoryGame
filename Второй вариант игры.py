x1 = [' ', ' ', ' ']
x2 = [' ', ' ', ' ']
x3 = [' ', ' ', ' ']
log = 'Сделайте свой ход, например, с помощью "a1", или "b3".'
game_ended = 0
turn = ''
turn_counter = 0
player_x_turn = 1
wrong_syntax = 0
cheat = 0

while game_ended == 0:

    print("   a  b  c")
    print("1 [", x1[0], "][", x1[1], "][", x1[2], "]", sep='')
    print("2 [", x2[0], "][", x2[1], "][", x2[2], "]", sep='')
    print("3 [", x3[0], "][", x3[1], "][", x3[2], "]", sep='')
    print()
    print('Gamelog: ', log, sep='')
    print()

    if wrong_syntax == 1:
        print("Ошибка ввода! Пожалуйста повторите.")

    if cheat == 1:
        print("поле занято")

    wrong_syntax = 0
    cheat = 0

    if player_x_turn == 1:
        print('Player X turn: ', sep='', end='')
    else:
        print('Player O turn: ', sep='', end='')

    turn = input()

    if len(turn) != 2:
        print('Введите не больше двух символов')
        continue

    if turn[0] == 'a' or turn[0] == 'b' or turn[0] == 'c':
        if turn[1] == '1' or turn[1] == '2' or turn[1] == '3':
            if log == 'Сделайте свой ход, например, с помощью "a1", или "b3".':
                log = ""

            if player_x_turn == 1:
                if turn[0] == 'a' and turn[1] == '1':
                    if x1[0] == " ":
                        x1[0] = "x"
                    else:
                        cheat = 1

            if player_x_turn == 1:
                if turn[0] == 'a' and turn[1] == '2':
                    if x2[0] == " ":
                        x2[0] = "x"
                    else:
                        cheat = 1

            if player_x_turn == 1:
                if turn[0] == 'a' and turn[1] == '3':
                    if x3[0] == " ":
                        x3[0] = "x"
                    else:
                        cheat = 1

            if player_x_turn == 1:
                if turn[0] == 'b' and turn[1] == '1':
                    if x1[1] == " ":
                        x1[1] = "x"
                    else:
                        cheat = 1

            if player_x_turn == 1:
                if turn[0] == 'b' and turn[1] == '2':
                    if x2[1] == " ":
                        x2[1] = "x"
                    else:
                        cheat = 1

            if player_x_turn == 1:
                if turn[0] == 'b' and turn[1] == '3':
                    if x3[1] == " ":
                        x3[1] = "x"
                    else:
                        cheat = 1

            if player_x_turn == 1:
                if turn[0] == 'c' and turn[1] == '1':
                    if x1[2] == " ":
                        x1[2] = "x"
                    else:
                        cheat = 1

            if player_x_turn == 1:
                if turn[0] == 'c' and turn[1] == '2':
                    if x2[2] == " ":
                        x2[2] = "x"
                    else:
                        cheat = 1

            if player_x_turn == 1:
                if turn[0] == 'c' and turn[1] == '3':
                    if x3[2] == " ":
                        x3[2] = "x"
                    else:
                        cheat = 1

            if player_x_turn == 0:
                if turn[0] == 'a' and turn[1] == '1':
                    if x1[0] == " ":
                        x1[0] = "o"
                    else:
                        cheat = 1

            if player_x_turn == 0:
                if turn[0] == 'a' and turn[1] == '2':
                    if x2[0] == " ":
                        x2[0] = "o"
                    else:
                        cheat = 1

            if player_x_turn == 0:
                if turn[0] == 'a' and turn[1] == '3':
                    if x3[0] == " ":
                        x3[0] = "o"
                    else:
                        cheat = 1

            if player_x_turn == 0:
                if turn[0] == 'b' and turn[1] == '1':
                    if x1[1] == " ":
                        x1[1] = "o"
                    else:
                        cheat = 1

            if player_x_turn == 0:
                if turn[0] == 'b' and turn[1] == '2':
                    if x2[1] == " ":
                        x2[1] = "o"
                    else:
                        cheat = 1

            if player_x_turn == 0:
                if turn[0] == 'b' and turn[1] == '3':
                    if x3[1] == " ":
                        x3[1] = "o"
                    else:
                        cheat = 1

            if player_x_turn == 0:
                if turn[0] == 'c' and turn[1] == '1':
                    if x1[2] == " ":
                        x1[2] = "o"
                    else:
                        cheat = 1

            if player_x_turn == 0:
                if turn[0] == 'c' and turn[1] == '2':
                    if x2[2] == " ":
                        x2[2] = "o"
                    else:
                        cheat = 1

            if player_x_turn == 0:
                if turn[0] == 'c' and turn[1] == '3':
                    if x3[2] == " ":
                        x3[2] = "o"
                    else:
                        cheat = 1

            if wrong_syntax == 0 and cheat == 0:
                turn_counter = turn_counter + 1
                if player_x_turn == 1:
                    log = log + str(turn_counter) + ") X: " + turn
                else:
                    log = log + str(turn_counter) + ") O: " + turn

            if wrong_syntax == 0 and cheat == 0:
                if player_x_turn == 1:
                    player_x_turn = 0
                else:
                    player_x_turn = 1


        else:
            wrong_syntax = 1
    else:
        wrong_syntax = 1

    print()

    if x1[0] == x1[1] and x1[0] == x1[2] and x1[0] == 'x':
        log = log + '. X победил!'
        game_ended = 1

    if x2[0] == x2[1] and x2[0] == x2[2] and x2[0] == 'x':
        log = log + '. X победил!'
        game_ended = 1

    if x3[0] == x3[1] and x3[0] == x3[2] and x3[0] == 'x':
        log = log + '. X победил!'
        game_ended = 1

    if x1[0] == x2[0] and x1[0] == x3[0] and x1[0] == 'x':
        log = log + '. X победил!'
        game_ended = 1

    if x1[1] == x2[1] and x1[1] == x3[1] and x1[1] == 'x':
        log = log + '. X победил!'
        game_ended = 1

    if x1[2] == x2[2] and x1[2] == x3[2] and x1[2] == 'x':
        log = log + '. X победил!'
        game_ended = 1

    if x1[0] == x2[1] and x1[0] == x3[2] and x1[0] == 'x':
        log = log + '. X победил!'
        game_ended = 1

    if x1[2] == x2[1] and x1[2] == x3[0] and x1[2] == 'x':
        log = log + '. X победил!'
        game_ended = 1

    if x1[0] == x1[1] and x1[0] == x1[2] and x1[0] == 'o':
        log = log + '. O победил!'
        game_ended = 1

    if x2[0] == x2[1] and x2[0] == x2[2] and x2[0] == 'o':
        log = log + '. O победил!'
        game_ended = 1

    if x3[0] == x3[1] and x3[0] == x3[2] and x3[0] == 'o':
        log = log + '. O победил!'
        game_ended = 1

    if x1[0] == x2[0] and x1[0] == x3[0] and x1[0] == 'o':
        log = log + '. O победил!'
        game_ended = 1

    if x1[1] == x2[1] and x1[1] == x3[1] and x1[1] == 'o':
        log = log + '. O победил!'
        game_ended = 1

    if x1[2] == x2[2] and x1[2] == x3[2] and x1[2] == 'o':
        log = log + '. O победил!'
        game_ended = 1

    if x1[0] == x2[1] and x1[0] == x3[2] and x1[0] == 'o':
        log = log + '. O победил!'
        game_ended = 1

    if x1[2] == x2[1] and x1[2] == x3[0] and x1[2] == 'o':
        log = log + '. O победил!'
        game_ended = 1

    if turn_counter == 9 and game_ended == 0:
        game_ended = 1
        log = log + '. Ничья!'

    if wrong_syntax == 0 and game_ended == 0 and cheat == 0:
        log = log + '; '

if game_ended == 1:
    print("   a  b  c")
    print("1 [", x1[0], "][", x1[1], "][", x1[2], "]", sep='')
    print("2 [", x2[0], "][", x2[1], "][", x2[2], "]", sep='')
    print("3 [", x3[0], "][", x3[1], "][", x3[2], "]", sep='')
    print()
    print('Gamelog: ', log, sep='')
    print()