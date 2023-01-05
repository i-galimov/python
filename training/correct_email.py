# Будем считать email адрес корректным, если в нем есть символ собачки (@) и точки. Напишите программу проверяющую корректность email адреса.

email = input()
if "@" in email and "." in email:
    print("YES")
else:
    print("NO")