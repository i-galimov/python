# Напишите функцию get_circle(radius), которая принимает в качестве аргумента радиус окружности и возвращает два значения: длину окружности и площадь круга, ограниченного данной окружностью.

# объявление функции
from math import pi

def get_circle(radius):
    S = pi*r ** 2
    C = 2*pi*r
    return C, S

# считываем данные
r = float(input())

# вызываем функцию
length, square = get_circle(r)
print(length, square)
