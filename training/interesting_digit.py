# Назовем число интересным, если в нем разность максимальной и минимальной цифры равняется средней по величине цифре. Напишите программу, которая определяет интересное число или нет. Если число интересное, следует вывести – «Число интересное» иначе «Число неинтересное».

a = abs(int(input()))
b = a // 100
c = (a % 100) // 10
d = a % 10 
ma = max(b, c, d)
mi = min(b, c, d)
sr = b + c + d - ma - mi
if sr == ma - mi:
    print("Число интересное")
else: 
    print("Число неинтересное")