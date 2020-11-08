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

	def discharge_inarabic(rom, discharge):	# rom от меньшего к большему, пример: CDM
		nonlocal answer
		nonlocal value
		rom = list(rom)
		X = ''

		def ent_check():
			nonlocal rom
			nonlocal value
			nonlocal X
			for any in rom:
				if value.startswith(any):
					X += value[0]
					value = value[1:]


		for _ in range(4):
			ent_check()

		if X.startswith(rom[0]):
			if len(X) == 2:
				if X[1] in rom[1]:
					answer += discharge * 4
				if X[1] in rom[2]:
					answer += discharge * 9
			if X in rom[0] * 3:
				answer += discharge * len(X)

		if X.startswith(rom[1]):
			if len(X) == 1:
				answer += discharge * 5
			if 1 < len(X) <= 4 and X[1:] in rom[0] * 3:
				answer += discharge * 5 + discharge * (len(X) - 1)

	discharge_inarabic('CDM', 100)
	discharge_inarabic('XLC', 10)
	discharge_inarabic('IVX', 1)

	if value:
		print('\nincorrect input')
		exit()

	if not answer:
		print('\nincorrect input')
		exit()

	return answer

# сокращаем дробь
arabic_answer = str(Fraction(inarabic(value[0]), inarabic(value[1]))).split('/')
arabic_answer = list(map(int, arabic_answer))

# go back in roman
def in_roman(value):
	answer = ''
	def discharge_inroman():
		nonlocal value
		nonlocal answer
		if len(str(value)) == 3:
			rom = list('CDM')
			discharge = 100
		if len(str(value)) == 2:
			rom = list('XLC')
			discharge = 10
		if len(str(value)) == 1:
			rom = list('IVX')
			discharge = 1

		if 5 <= value // discharge <= 8:
			answer += rom[1]
			if 6 <= value // discharge <= 8:
				keks = value // discharge - 5
				answer += rom[0] * keks

		if 1 <= value // discharge <= 3:
			answer += rom[0] * (value // discharge)

		if value // discharge == 4:
			answer += rom[0]
			answer += rom[1]

		if value // discharge == 9:
			answer += rom[0]
			answer += rom[2]

		value = value - (value // discharge * discharge)

	for_range = len(str(value))
	for _ in range(for_range):
		discharge_inroman()

	return answer

# ответыч
print(f'\nответ: {in_roman(arabic_answer[0])}/{in_roman(arabic_answer[1])}')
