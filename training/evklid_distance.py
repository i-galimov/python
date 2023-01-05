# Напишите программу определяющую евклидово расстояние между двумя точками, координаты которых заданы.

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
from math import *
l = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
print(l)