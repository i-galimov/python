# На вход программе подается натуральное число n, а затем n целых чисел, каждое на отдельной строке. Напишите программу, которая подсчитывает сумму введенных чисел. 

total = 0
n = int(input())
for i in range(n):
    num = int(input())
    total += num
print(total)