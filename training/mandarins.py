# n школьников делят kk мандаринов поровну, неделящийся остаток остается в корзине. Сколько целых мандаринов достанется каждому школьнику? Сколько целых мандаринов останется в корзине?

#Формат входных данных
#На вход программе подаётся два целых числа: количество школьников и количество мандаринов, каждое на отдельной строке.

#Формат выходных данных
#Программа должна вывести два числа: количество мандаринов, которое достанется каждому школьнику, и количество мандаринов, которое останется в корзине, каждое на отдельной строке.

a = int(input())
b = int(input())
print(b // a)
print(b % a)