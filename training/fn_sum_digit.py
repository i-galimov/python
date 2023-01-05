# Напишите функцию print_digit_sum(), которая принимает одно целое число n и выводит на печать сумму его цифр.

# объявление функции
def print_digit_sum(n):
    sum = 0
    txt = str(n)
    nums = [int(txt[i]) for i in range(len(txt))]
    for j in range(len(nums)):
        sum += nums[j]
    print(sum)
    
# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)
