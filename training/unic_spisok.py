# На вход программе подается натуральное число n, а затем n строк. Напишите программу, которая выводит только уникальные строки, в том же порядке, в котором они были введены.

from  more_itertools import unique_everseen
n = int(input())
nums = [input() for i in range(n)]
txt = list(unique_everseen(nums))
print(*txt, sep='\n')
