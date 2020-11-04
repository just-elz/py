# 6. Вывести все элементы списка, стоящие до максимального элемента

# ввод значений
value = input('enter values: ')
value = value.replace(' ', '').replace('.', ',')

check = value.replace(',', '').replace('-', '')
if not check.isdigit():			# проверка корректности
	print('\nincorrect input')
	exit()

value = value.split(',')
value = list(map(int, value))
answer = []
max_num = sorted(value)[-1]
for any in value:
	if any == max_num:
		break
	answer.append(any)

print('ответ: ', answer)
