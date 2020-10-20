# перевод двузначного числа написаного цифрами в пропись
print('this programm will help u display numbers in writing')

# ввод числа
a = input("\nlet's start - enter a number from 0 to 99: ")
a = a.strip()

# проверка введенных данных
if not 1 <= len(a) <= 2:
	print('\nincorrcet input')
	input('\nPress any key to exit')
	exit()
	
if not a.isdigit():
	print('\nincorrcet input')
	input('\nPress any key to exit')
	exit()

# перевод числа в пропись
a = int(a)

b = ''					# ввели переменную для ответа

if a // 10 == 2:		# переводим десятки в пропись
	b += 'двадцать '
elif a // 10 == 3:
	b += 'тридцать '
elif a // 10 == 4:
	b += 'сорок '
elif a // 10 == 5:
	b += 'пятьдесят'
elif a // 10 == 6:
	b += 'шестьдесят '
elif a // 10 == 7:
	b += 'семьдесят '
elif a // 10 == 8:
	b += 'восемьдесят '
elif a // 10 == 9:
	b += 'девяносто '

if a == 10:				# переводим числа на -дцать и 0 в пропись
	b += 'десять'
elif a == 11:
	b += 'одинадцать'
elif a == 12:
	b += 'двенадцать'
elif a == 13:
	b += 'тринадцать'
elif a == 14:
	b += 'четырнадцать'
elif a == 15:
	b += 'пятнадцать'
elif a == 16:
	b += 'шестнадцать'
elif a == 17:
	b += 'семнадцать'
elif a == 18:
	b += 'восемнадцать'
elif a == 19:
	b += 'девятнадцать'
elif a == 0:
	b += 'ноль'

elif a % 10 == 1:			# переводим единицы в пропись
	b += 'один'
elif a % 10 == 2:
	b += 'два'
elif a % 10 == 3:
	b += 'три'
elif a % 10 == 4:
	b += 'четыре'
elif a % 10 == 5:
	b += 'пять'
elif a % 10 == 6:
	b += 'шесть'
elif a % 10 == 7:
	b += 'семь'
elif a % 10 == 8:
	b += 'восемь'
elif a % 10 == 9:
	b += 'девять'

# вывод ответа
if b:
	print('\nanswer: ', b)
else:

	print('\nincorrcet input')
	input('\nPress any key to exit')
	exit()

input('\nPress any key to exit')
