# 2. Дан список целых чисел, в котором есть нулевые элементы. Исключить нулевые элементы.

# ввод значений
value = input("enter values separated by dot or comma: ")
value = value.replace(' ', '').replace('.', ',').strip('.,')
check = value.replace(',','').replace('-', '')

if not check.isdigit():
	print('\nincorrcet input')
	input('\nPress any key to exit')
	exit()

if len(check) > 100:
	print('\nincorrcet input')
	input('\nPress any key to exit')
	exit()

value = value.split(',')
answer = []
for _ in value:
	if _ == 0:
		continue
	if _ == '':
		continue
	answer.append(_)

print('\nОтвет:', answer)
input()
