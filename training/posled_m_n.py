# Даны два целых числа m и n. Напишите программу, которая выводит все числа от m до n включительно в порядке возрастания, если m < n, или в порядке убывания в противном случае.

m = int(input())
n = int(input())
if m > n:
  for i in range(m, n - 1, -1):
    print(i)
else:
  for i in range(m, n + 1):
    print(i)