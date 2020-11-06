# 9. Исключить из списка элементы, расположенные между максимальным и минимальным.
# (для тех кому сложно сделать в общем случап, берите самый первый минимальный элемент и первый максимальный)

# ____________________________________simple_version________________________________________

# ввод значений
# value = input('enter values: ')
# value = value.replace(' ', '').replace('.', ',')

# # проверка корректности
# check = value.replace(',', '').replace('-', '')
# if not check.isdigit():
# 	print('\nincorrect input')
# 	exit()

# value = value.split(',')
# value = list(map(int, value))

# min_num = sorted(value)[0]
# max_num = sorted(value)[-1]

# id_max = value.index(max_num)
# id_min = value.index(min_num)

# del value[id_max:id_min + 1]

# print('ответ: ', value)

# ___________________________________________________________________________________________

# ввод значений
value = input('enter values: ')
value = value.replace(' ', '').replace('.', ',').strip('.,')

# проверка корректности
check = value.replace(',', '').replace('-', '')
if not check.isdigit():
	print('\nincorrect input')
	exit()

# присвоили данным тип int
value = value.split(',')
value = list(map(int, value))

# нашли макс и мин элементы в списке
max_num = sorted(value)[-1]
min_num = sorted(value)[0]

# выписываем indexes макс и мин значений
idxs_max = list(any for any in range(len(value)) if value[any] == max_num)			# СЛАВА МАКСИМУ ПЕНЗИНУ
idxs_min = list(any for any in range(len(value)) if value[any] == min_num)

# удаляем элементы между макс. и минимальным значением
# переменные для срезов
max0 = idxs_max[0]
min0 = idxs_min[0]

# временные переменные
max1 = None
min1 = None
just_list = []
max_cut = []
min_cut = []

while True:
	if max0 == idxs_max[-1]:			# условие для последнего среза
		max_cut.append(max0 + 1)
		min_cut.append(min0)
		break

	for any in idxs_max:			# обозначили будущий макс.индекс для след.цикла
		if any > min0:
			max1 = any
			break

	for any in idxs_min:			# "подбиваем" минимальное значение в текущем цикле
		if any < max1:
			just_list.append(any)
	min0 = just_list[-1]

# в этом месте я должен был удалять лишнее, но я идиот и пошел с начала, а не с конца
# поэтому резать мы будем дальше))))))))))))))))))))))))))))
# а сейчас просто добавим индексы по которым будем резать список

	max_cut.append(max0 + 1)
	min_cut.append(min0)

	for any in idxs_min:			# обозначили мин.индекс для след. цикла
		if any > max1:
			min0 = any
			break

	max0 = max1			# обозначили макс.индекс для след.цикла


# вырезаем все лишнее
zip_list = list(zip(max_cut, min_cut))
zip_list.reverse()			# делаем это с конца))))))))0
for any in zip_list:
	del value[any[0]:any[1]]

print(f'\nответ: {value}')
