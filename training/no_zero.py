# Напишите программу, которая считывает 10 чисел и выводит произведение отличных от нуля чисел.

result = 1 
for _ in range(10): 
    a = int(input()) 
    if a != 0: 
        result *= a 
print(result)
