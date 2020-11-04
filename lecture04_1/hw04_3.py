# 3. Дан список X целых чисел и целое число b. Исключить из списка элементы, равные b.

# ввод значений
value = input("enter values separated by dot or comma: ")
value = value.replace(' ', '').replace('.', ',').strip('.,')

b = input('enter number b: ')
if not b.isdigit():
	print('\nincorrcet input')
	input('\nPress any key to exit')
	exit()

check = value.replace(',','').replace('-', '')

if not check.isdigit():
	print('\nincorrcet input')
	input('\nPress any key to exit')
	exit()

if len(check) > 100:
	print('\nincorrcet input')
	input('\nPress any key to exit')
	exit()

answer = value.split(',')
answer.remove(b)

print('\nОтвет:', answer)
input()
