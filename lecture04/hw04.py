# нахождение простых чисел используя решето Эратосфена
print("this programm will help u find prime numbers")

# ввод значения и его проверка
n = input("\nlet's start - enter an integer greater than 2: ")
n = n.replace(' ', '')

if not n.isdigit():
	print('\nincorrcet input')
	input('\nPress any key to exit')
	exit()

if len(n) <= 1 and n not in '23456789':
	print('\nincorrcet input')
	input('\nPress any key to exit')
	exit()

if len(n) > 6:
	print('\nincorrcet input')
	input('\nPress any key to exit')
	exit()

# нахождение простых чисел через решето
n = list(range(2, int(n)+1))
p = []
answer = []

while n:
	for i in n:
		if i % n[0] == 0:
			p.append(i)
	answer.append(n[0])
	n = list(set(n) - set(p))

answer.sort()

with open('answer.txt', 'w') as f:
	for a in answer:
		f.write(f'{a}\n')
