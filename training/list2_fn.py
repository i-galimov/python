# На вход программе подается натуральное число n, а затем n целых чисел. Напишите программу, которая для каждого введенного числа xx выводит значение функции f(x) = x^2 + 2x + 1 каждое на отдельной строке.

n = int(input())
nums = [int(input()) for i in range(n)]
print(*nums, sep='\n')
print()
nums2 = [nums[i] ** 2 + 2 * nums[i] + 1 for i in range(n)]
print(*nums2, sep='\n')
