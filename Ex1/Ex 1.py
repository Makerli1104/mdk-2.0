import math 
#1)реализовать обмен значений переменных без использования третьей

a=int(input())
b=int(input())
a=a+b
b=a-b
a=a-b
print(a,b)

#2)найдите сумму чисел введённого числа

print(sum(map(int, list(input()))))

#3)найти корни квадратного уравнения

import math
a = int(input(" a= "))
b = int(input(" b= "))
c = int(input(" c= "))
D = b ** 2 - 4 * a * c
print(D)
if D < 0:
  print("Нет корней")
elif D == 0:
  x = -b / 2 * a
  print (x)
else:
  x1 = (-b + math.sqrt(D)) / (2 * a)
  x2 = (-b - math.sqrt(D)) / (2 * a)
  print(x1)
  print(x2)