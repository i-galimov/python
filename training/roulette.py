# На колесе рулетки карманы пронумерованы от 0 до 36. Ниже приведены цвета карманов: карман 0 зеленый; для карманов с 1 по 10 карманы с нечетным номером имеют красный цвет, карманы с четным номером – черный; для карманов с 11 по 18 карманы с нечетным номером имеют черный цвет, карманы с четным номером – красный; для карманов с 19 по 28 карманы с нечетным номером имеют красный цвет, карманы с четным номером – черный; для карманов с 29 по 36 карманы с нечетным номером имеют черный цвет, карманы с четным номером – красный.
# Напишите программу, которая считывает номер кармана и показывает, является ли этот карман зеленым, красным или черным. Программа должна вывести сообщение об ошибке, если пользователь вводит число, которое лежит вне диапазона от 0 до 36.

num = int(input())
green = [0]
red = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
black = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
if num in red:
  print("красный")
elif num in black:
  print("черный")
elif num in green:
  print("зеленый")
else:
  print("ошибка ввода")
