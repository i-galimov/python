# На вход программе подается натуральное число n, а затем nn строк. Напишите программу, которая создает из указанных строк список и выводит его.

spisok = list()
n = int(input())
for i in range(n):
  spisok.append(input())
print(spisok)
