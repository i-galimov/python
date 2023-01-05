# Напишите функцию get_days(month), которая принимает в качестве аргумента номер месяца и возвращает количество дней в данном месяце.

# объявление функции
def get_days(month):
    day31 = [1, 3, 5, 7, 8, 10, 12]
    day30 = [4, 6, 9, 11]
    day28 = [2]
    if month in day31:
        return 31
    elif month in day30:
        return 30
    else:
        return 28

# считываем данные
num = int(input())

# вызываем функцию
print(get_days(num))
