# При анализе данных, собранных в рамках научного эксперимента, бывает полезно удалить самое большое и самое маленькое значение.

# На вход программе подается натуральное число n, а затем n различных натуральных чисел. Напишите программу, которая удаляет наименьшее и наибольшее значение из указанных чисел, а затем выводит оставшиеся числа каждое на отдельной строке, не меняя их порядок.

n = int(input())
nums = [int(input()) for i in range(n)]
a = max(nums)
b = min(nums)
nums.remove(a)
nums.remove(b)
print(*nums, sep='\n')
