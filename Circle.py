#Code to find the circumference and area of a circle of a given radius

import math
x = int(input("Enter a digit: "))

circumference = x*2*math.pi
area = x*x*2*math.pi
print(circumference, area)
print(f'{circumference}\n{area}')
