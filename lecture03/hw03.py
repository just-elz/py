# перевод градусов из одной системы ед. в другую
print("this programm will help u display degrees of\
 one system of units to another")

# ввод значения и его проверка
value = input("\nlet's start - enter degrees with unit designation(F/C): ")
value = value.replace(' ', '').replace(',', '.').replace('+', '')
if len(value) > 12:
	print('\nincorrcet input')
	input('\nPress any key to exit')
	exit()

# перевод градусов
degree, unit = value[:-1], value[-1]
answer = None

if degree[0] not in '-':		# блок для положительных значений
	if unit in 'fF' and degree.replace('.', '', 1).isdigit():
		answer = float(degree)
		print('\nanswer: ', answer * 9 / 5 + 32,'C')
	elif unit in 'cC' and degree.replace('.', '', 1).isdigit():
		answer = float(degree)
		print('\nanswer: ', (answer - 32) * 5 / 9,'F')

if degree[0] in '-':			# блок для отрицательных значений
	degree = degree[1:]
	if unit in 'fF' and degree[1:].replace('.', '', 1).isdigit():
		answer = -float(degree)
		print('\nanswer: ', answer * 9 / 5 + 32,'C')
	elif unit in 'cC' and degree[1:].replace('.', '', 1).isdigit():
		answer = -float(degree)
		print('\nanswer: ', (answer - 32) * 5 / 9,'F')

if not answer:
	print('\nincorrcet input')
	input('\nPress any key to exit')
	exit()

input('\nPress any key to exit')
