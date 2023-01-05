# На вход программе подается натуральное число n, а затем n целых чисел. Напишите программу, которая сначала выводит все отрицательные числа, затем нули, а затем все положительные числа, каждое на отдельной строке. Числа должны быть выведены в том же порядке, в котором они были введены.

n = int(input())
nums = [int(input()) for i in range(n)]
negative = [nums[j] for j in range(n) if nums[j] < 0]
print(*negative, sep='\n')
zero = [nums[k] for k in range(n) if nums[k] == 0]
print(*zero, sep='\n')
positive = [nums[j] for j in range(n) if nums[j] > 0]
print(*positive, sep='\n')
