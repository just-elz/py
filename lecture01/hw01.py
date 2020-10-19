# нахождение третей стороны через теорему косинуса

import math

# вводим значения
a = float(input("enter the value of the first side: "))
print("first side =", a)

b = float(input("enter the value of the second side: "))
print("second side =", b)

c = float(input("enter the angle between the sides: "))
print("angle betweed sides =", c)

# вывод ответа
print("so, third side =",
	math.sqrt(a**2 + b**2 - 2*a*b*math.cos(math.radians(c))))

input('Press any key to exit')
