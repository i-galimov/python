# Напишите программу, которая упорядочивает три числа от большего к меньшему.

a = int(input())
b = int(input())
c = int(input())
spis = [a, b, c]
spis.sort(reverse=True)
print(spis[0])
print(spis[1])
print(spis[2])