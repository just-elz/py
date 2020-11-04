# 4. Дан список целых чисел и числа A1, A2 и A3. Включить эти числа в список, расположив их после второго элемента.

# ввод значений
value = input('enter values: ')
value = value.replace(' ', '').replace('.', ',')
A1 = input('\nenter A1: ')
A2 = input('\nenter A2: ')
A3 = input('\nenter A3: ')

def isdig(_):			# функция для проверки(число ли)
	if not _.isdigit():
		print('\nincorrect input')
		exit()

# проверка всех входных данных на число
check = value.replace(',', '').replace('-', '')
isdig(check)
isdig(A1)
isdig(A2)
isdig(A3)

# удаление пустых значений из value
# p.s.не бейте по рукам, я знаю шо так низя xd
value = value.split(',')
while '' in value:
		value.remove('')

# добавление чисел
value.insert(2, A3)
value.insert(2, A2)
value.insert(2, A1)

print('\nответ: ', value)

input()
