# На вход программе подается натуральное число n. Напишите программу, которая подсчитывает сумму тех чисел от 1 до n (включительно) квадрат которых оканчивается на 2, 5 или 8.

n = int(input())
total = 0
for i in range(n + 1):
    if i ** 2 % 10 == 2 or i ** 2 % 10 == 5 or i ** 2 % 10 == 8:
        total += i
print(total) 
