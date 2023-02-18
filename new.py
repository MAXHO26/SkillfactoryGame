field_size = 3
field = [1,2,3,4,5,6,7,8,9]
x = 0
a = [1,2,3]

def draw_field():
	print(f"{'---▼' * field_size}---")
	for i in range(field_size):
		print (f"►| {field[i * 3]} | {field[1 + i * 3]} | {field[2 + i * 3]} | ")

def check_winners():

	win = False

	win_combo = (
		(0,1,2), (3,4,5), (6,7,8),
		(0,3,6), (1,4,7), (2,5,8),
		(0,4,8), (2,4,6)
	)

	for pos in win_combo:
		if (field[pos[0]] == field[pos[1]] and\
			field[pos[1]] == field[pos[2]] and\
			field[pos[1]] in ('X','O')):
				win = field[pos[0]]

	return win

def game_steps(index, char):
	if (index > 10 or index < 1 or\
		field[index-1] in ('X','O')):
			return False

	field[index-1] = char
	return True

def start_game():
	current_player = 'X'
	step = 1
	draw_field()
	while (step < 9) and (check_winners() == False):
		index = input('Ходит игрок:' + current_player + '. Введите номер поля:\n')

		if len(index) != 1:
			print('Введите номер поля')
			continue

		if not (index[0].isdigit()):
			print('Введите число')
			continue

		if (game_steps(int(index), current_player)):
			print('Обновленное поле:')

			if (current_player == 'X'):
				current_player = 'O'
			else:
				current_player = 'X'

			draw_field()
			step += 1
		else:
			print('Поле занято! Повторите!')

	if (step == 9):
		print('Игра оконцена. Ничья!')
	else:
		print('Выиграл ' + check_winners())
print("\n")
print('Право первого хода за игроком (Х)')
print('Сделайте первый ход в диапазоне чисел от 1 до 9:')
start_game()