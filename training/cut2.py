# На вход программе подается одна строка. Напишите программу, которая выводит: третий символ этой строки; предпоследний символ этой строки; первые пять символов этой строки;всю строку, кроме последних двух символов; все символы с четными индексами; все символы с нечетными индексами; все символы в обратном порядке; все символы строки через один в обратном порядке, начиная с последнего.

txt = input()
print(txt[2])
print(txt[-2])
print(txt[0:5])
print(txt[:-2])
l = len(txt)
print(txt[0:l:2])
print(txt[1:l:2])
print(txt[::-1])
print(txt[::-2])
