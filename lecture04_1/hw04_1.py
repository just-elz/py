n = input("enter values separated by dot or comma: ")
n = n.replace(' ', '').replace('.', ',').strip('.,')
check = n.replace(',','').replace('-', '')

if not check.isdigit():
	print('\nincorrcet input')
	input('\nPress any key to exit')
	exit()

if len(check) > 100:
	print('\nincorrcet input')
	input('\nPress any key to exit')
	exit()

n = n.split(',')
print(n)
answer = []
for _ in n:
	if _ == '':
		continue
	answer.append(_)
answer = [int(_) for _ in answer]
answer = sorted(answer)

print(answer)
answerA = answer[:-1]
print('\na)',answerA)

answerB = answer[1:]
print('\nb)',answerB)
input()
