# Задача 4 (опциональная)
# Необходимо сократить дробь, записанную в римской системе счисления (числа от 1 до 999).

# Римская система счисления: 
'''https://ru.wikipedia.org
/wiki/%D0%A0%D0%B8%D0%BC%D1%81%D0%BA%D0%B8%D0%B5_%D1%86%D0%B8%D1%84%D1%80%D1%8B
'''

# Ввод: "II/IV"
# Вывод: "I/II"

# Ввод: "XXIV/VIII"
# Вывод: "III"

# Ввод: "12/16"
# Вывод: "ERROR"

# ___________________________________________________________________________________________
from fractions import Fraction

# ввод данных
value = input('enter values: ').replace(' ', '').split('/')

# проверка корректности
check = list(map(list, value))
if len(check) != 2:
	print('\nincorrect input')
	exit()

def isroman(num):
	for any in num:
		if any not in 'IVXLCDM':
			print('\nincorrect input')
			exit()

isroman(check[0])
isroman(check[1])

# перевод римских чисел в арабские
def inarabic(value):
	answer = 0
	hundreds = {
	'C': 100,
	'CC': 200,
	'CCC': 300,
	'CD': 400,
	'D': 500,
	'DC': 600,
	'DCC': 700,
	'DCCC': 800,
	'CM': 900,
}
	for any in sorted(hundreds, key=len, reverse=True):
		if value.startswith(any):
			if answer < 100:
				answer += hundreds[any]
				value = value[len(any):]
			else:
				print('\nincorrect input')
				exit()

	tens = {
	'X': 10,
	'XX': 20,
	'XXX': 30,
	'XL': 40,
	'L': 50,
	'LX': 60,
	'LXX': 70,
	'LXXX': 80,
	'XC': 90,
}
	for any in sorted(tens, key=len, reverse=True):
		if value.startswith(any):
			if str(answer)[1] == '0':
				answer += tens[any]
				value = value[len(any):]
			else:
				print('\nincorrect input')
				exit()

	units = {
	'I': 1,
	'II': 2,
	'III': 3,
	'IV': 4,
	'V': 5,
	'VI': 6,
	'VII': 7,
	'VIII': 8,
	'IX': 9,
}
	for any in sorted(units, key=len, reverse=True):
		if value.startswith(any):
			if str(answer)[-1] == '0':
				answer += units[any]
				value = value[len(any):]
			else:
				print('\nincorrect input')
				exit()

	return answer

# сокращаем дробь
arabic_answer = str(Fraction(inarabic(value[0]), inarabic(value[1]))).split('/')
arabic_answer = list(map(int, arabic_answer))

# go back in roman
def inroman(value):
	answer = ''
	def vpadlu1(value, arab, rom):
		nonlocal answer
		if value == arab:
			answer += rom
	if value > 99:
		hundred = value - value % 100
		vpadlu1(hundred, 100, 'C')
		vpadlu1(hundred, 200, 'CC')
		vpadlu1(hundred, 300, 'CCC')
		vpadlu1(hundred, 400, 'CD')
		vpadlu1(hundred, 500, 'D')
		vpadlu1(hundred, 600, 'DC')
		vpadlu1(hundred, 700, 'DCC')
		vpadlu1(hundred, 800, 'DCCC')
		vpadlu1(hundred, 900, 'CM')
		value = value % 100

	if value > 9:
		ten = value - value % 10
		vpadlu1(ten, 10, 'X')
		vpadlu1(ten, 20, 'XX')
		vpadlu1(ten, 30, 'XXX')
		vpadlu1(ten, 40, 'XL')
		vpadlu1(ten, 50, 'L')
		vpadlu1(ten, 60, 'LX')
		vpadlu1(ten, 70, 'LXX')
		vpadlu1(ten, 80, 'LXX')
		vpadlu1(ten, 90, 'XC')
		value = value % 10

	vpadlu1(value, 1, 'I')
	vpadlu1(value, 2, 'II')
	vpadlu1(value, 3, 'III')
	vpadlu1(value, 4, 'IV')
	vpadlu1(value, 5, 'V')
	vpadlu1(value, 6, 'VI')
	vpadlu1(value, 7, 'VII')
	vpadlu1(value, 8, 'VIII')
	vpadlu1(value, 9, 'IX')

	return answer

# ответыч
print(f'\nответ: {inroman(arabic_answer[0])}/{inroman(arabic_answer[1])}')
