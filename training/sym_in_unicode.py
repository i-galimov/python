# На вход программе подается строка текста. Напишите программу, которая переводит каждый ее символ в соответствующий ему код из таблицы символов Unicode.

a = input()
for i in range(len(a)):
  print(ord(a[i]), end=" ")