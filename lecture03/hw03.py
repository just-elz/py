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

if unit in 'fF':
	if degree.replace('.', '', 1).isdigit() or \
	degree[0] in '-' and degree[1:].replace('.', '', 1).isdigit():
		answer = float(degree)
	if answer:
		print('\nanswer: ', answer * 9 / 5 + 32,'C')

if unit in 'cC':
	if degree.replace('.', '', 1).isdigit() or \
	degree[0] in '-' and degree[1:].replace('.', '', 1).isdigit():
		answer = float(degree)
	if answer:
		print('\nanswer: ', (answer - 32) * 5 / 9,'F')

if not answer:
	print('\nincorrcet input')
	input('\nPress any key to exit')
	exit()

input('\nPress any key to exit')
