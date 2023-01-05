# Напишите функцию get_factors(num), принимающую в качестве аргумента натуральное число и возвращающую список всех делителей данного числа.

def get_factors(num):
    nums = []
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            nums.append(i)
    nums.append(num)
    return nums

# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))
