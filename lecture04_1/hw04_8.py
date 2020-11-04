# 8. Дан список из 10-ти чисел. Вычислить среднее арифметическое положительных элементов этого списка и среднее арифметическое отрицательных элементов этого списка

# ввод значений
value = input('enter values: ')
value = value.replace(' ', '').replace('.', ',')

# проверка корректности
check = value.replace(',', '').replace('-', '')
if not check.isdigit():
	print('\nincorrect input')
	exit()

value = value.split(',')
value = list(map(int, value))
if len(value) != 10:			# ещё небольшая проверка
	print('\nincorrect input')
	exit()

positive = []
negative = []
pos_sum = 0
neg_sum = 0
for any in value:
	if any > 0:
		positive.append(any)
		pos_sum += any
	if any < 0:
		negative.append(any)
		neg_sum += any

print(f'ответ: среднее арифметическое для положительных элементов {pos_sum/len(positive)},\
	среднее арифметическое для отрицательных элементов {neg_sum/len(negative)}')
