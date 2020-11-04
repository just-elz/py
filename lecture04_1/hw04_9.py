# 9. Исключить из списка элементы, расположенные между максимальным и минимальным.
# (для тех кому сложно сделать в общем случап, берите самый первый минимальный элемент и первый максимальный)

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

min_num = sorted(value)[0]
max_num = sorted(value)[-1]

id_max = value.index(max_num)
id_min = value.index(min_num)

del value[id_max:id_min + 1]

print('ответ: ', value)
