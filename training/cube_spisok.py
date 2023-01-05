# На вход программе подается строка текста, содержащая целые числа. Напишите программу, использующую списочное выражение, которая выведет кубы указанных чисел также на одной строке.

numbers = input().split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
num = [numbers[j] ** 3 for j in range(len(numbers))]
print(*num)
