# Напишите программу, вычисляющую объём куба и площадь его полной поверхности, по введённому значению длины ребра.
# На вход программе подается одно целое число – длина ребра.

a = int(input())
V = a*a*a
print("Объём =", V)
S = 6*a*a
print("Площадь полной поверхности =", S)