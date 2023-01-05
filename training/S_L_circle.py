# Напишите программу определяющую площадь круга и длину окружности по заданному радиусу.

R = float(input())
from math import *
S = pi*R ** 2
C = 2*pi*R
print(S)
print(C)