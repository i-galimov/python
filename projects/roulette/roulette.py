import random
import webbrowser
import time

def ask_yes():
    answer = input("Приветствую, искатель приключений. Предлагаю сыграть в русскую рулетку. Хочешь попробовать?\n")
    answer = answer.lower()
    answer_flag = 0
    while answer_flag == 0:
        if answer.lower() == "да":
            print("Класс!\n")
            answer_flag = 2
            return 1
        elif answer.lower() == "нет":
            print("Душнилы ответ!")
            time.sleep(2)
            answer_flag = 1
            webbrowser.open("https://youtu.be/dQw4w9WgXcQ")
            exit()
            return 0
        else:
            answer = input("Напиши 'Да' или 'Нет'\n ")
            answer = answer.lower()
            
def roulette():
    a = random.randint(20, 99)
    b = 0
    print("Поздравляю, тебе выпало число '", a, "\'!", sep='')
    while a > 0:
        webbrowser.open_new("https://en.m.wikipedia.org/wiki/" + str(b))
        try:
            c = open(str(b), "x")
        except:
        	pass
        a -= 1
        b +=1
 
ask_yes()
roulette()
