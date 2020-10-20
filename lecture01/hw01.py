# нахождение третей стороны через теорему косинуса
print('this programm will help u find third sid with using the cosine theorem')
import math

# вводим значения
a = float(input("\nlet's start - enter the value of the first side: "))

b = float(input("\nenter the value of the second side: "))

c = float(input("\nenter the angle between the sides: "))

# вывод ответа
print("\nso, third side =",
	math.sqrt(a**2 + b**2 - 2*a*b*math.cos(math.radians(c))))

input('\nPress any key to exit')
