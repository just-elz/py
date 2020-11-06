# 7. Дан список из 20-ти чисел и число A. Вычислить сумму тех отрицательных элементов списка, значения которых больше, чем A. Подсчитать также количество таких элементов.

# ввод значений
value = input('enter values: ')
value = value.replace(' ', '').replace('.', ',')
A = input('enter A: ')

# проверка корректности
check = value.replace(',', '').replace('-', '')
if not check.isdigit():
	print('\nincorrect input')
	exit()

if not A.replace('-', '').isdigit():
	print('\nincorrect input')
	exit()

A = int(A)
value = value.split(',')
value = list(map(int, value))
if len(value) != 20:			# ещё небольшая проверка
	print('\nincorrect input')
	exit()

for_sum = []			# переменная для нужных элементов

for any in value:
	if A < any < 0:
		for_sum.append(any)

sum = 0
for any in for_sum:
	sum += any

print(f'\nответ: сумма отрицательных элементов {sum}, количество таких элементов {len(for_sum)}')
