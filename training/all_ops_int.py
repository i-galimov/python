# Дано натуральное число. Напишите программу, которая вычисляет: сумму его цифр; количество цифр в нем; произведение его цифр; среднее арифметическое его цифр; его первую цифру; сумму его первой и последней цифры.

a  = input()
num = [int(nums) for nums in a]
l =len(num)
total = 0
multy = 1
for i in num:
  total += i
  multy *= i
print(total)
print(l)
print(multy)
print(total / l)
print(num[0])
print(num[0] + num[-1])
