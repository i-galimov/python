# Напишите программу, которая считывает три числа и подсчитывает сумму только положительных чисел.

a = int(input())
b = int(input())
c = int(input())
if a >= 0:
    a = a
else: 
    a = 0
if b >= 0:
    b = b
else: 
    b = 0
if c >= 0:
    c = c
else: 
    c = 0
print(a + b + c)