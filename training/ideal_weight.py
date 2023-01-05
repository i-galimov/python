print("Посчитаем индекс ваш идеальный вес")
height = int(input("Введите Ваш рост в сантиметрах\n"))
gender = input('Введите "М", если Вы - мужчина и "Ж", если Вы - женщина\n')
if gender in ["М", "м"]:
    ideal_weight = (height - 100)*0.9
    print("Ваш идеальный вес", ideal_weight, "килограмм")
elif gender in ["Ж", "ж"]:
    ideal_weight = (height - 100)*0.85
    print("Ваш идеальный вес", ideal_weight, "килограмм")
