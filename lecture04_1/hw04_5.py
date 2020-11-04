# Задан список из целых чисел. Переместить все минимальные элементы в начало списка, не меняя порядок других.
# 6 -3 -7 4 -7 -4 5 => -7 -7 6 -3 4 -4 5

# ввод значений
value = input('enter values: ')
value = value.replace(' ', '').replace('.', ',')

check = value.replace(',', '').replace('-', '')
if not check.isdigit():			# проверка корректности
	print('\nincorrect input')
	exit()

value = value.split(',')
value = list(map(int, value))

min_num = sorted(value)[0]
without_min_num = []
answer = []
for any in value:
	if any == min_num:
		answer.append(any)
		continue
	without_min_num.append(any)

print('\nответ: ', answer + without_min_num)
