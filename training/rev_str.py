# На вход программе подается одна строка. Напишите программу, которая выводит в столбик элементы строки в обратном порядке.

a = input()
for i in range(-1, -len(a)-1, -1):
  print(a[i])