# На вход программе подается натуральное число n. Напишите программу вычисления знакочередующей суммы

n = int(input())
posit = [i for i in range(1, n+1) if i % 2 != 0]
negat = [i * (-1) for i in range(1, n + 1) if i % 2 == 0]
res = sum(posit) + sum(negat)
print(res)
