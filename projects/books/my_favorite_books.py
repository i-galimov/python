import webbrowser
import time

class User(object):
    def __init__(self, name):
        self.name = name
    def get_name(self):
        print(self.name)

class Zhanr(object):
    #Конструктор Zhanr
    def __init__(self, name, count):
        self.name = name
        self.count = count
    #Геттеры Zhanr
    def get_name(self):
        print(self.name)
    def get_count(self):
        print(self.count)
    #Сеттеры Zhanr
    def set_name(self, name):
        self.name = name
    def set_count(self, count):
        self.count = count
        
    #Классы внутри Zhanr (композиция)
    class Book(object):
    #Конструктор Book
        def __init__(self, name, author, rate, url):
            self.name = name
            self.author = author
            self.rate = rate
            self.url = url
    #Геттеры Book
        def get_name(self):
            print(self.name)
        def get_author(self):
            print(self.author)
        def get_rate(self):
            print(self.rate)
        def get_url(self):
            print(self.url)
    #Сеттеры Book
        def set_name(self, name):
            self.name = name
        def set_author(self, author):
            self.author = author
        def set_rate(self, rate):
            self.rate = rate
        def set_url(self, url):
            self.url = url
    #Другие методы Book
        def print_info(self):
            print(self.rate, ".", '\"', self.name, '\" - ',  self.author, sep='')
        def run_info(self):
        	webbrowser.open(self.url)
 
class Recommend(Zhanr):
    def __init__(self, name, author):
        self.name = name
        self.author = author
    #Геттеры Recommend
    def get_author(self):
        print(self.author)
    #Сеттеры Zhanr
    def set_author(self, author):
        self.author = author

print("Приветствую, искатель приключений.\n");
NewUser = User(input("Давай познакомимся, как тебя зовут?\n"))

print("Очень приятно, ", NewUser.name,", а меня зовут Ильшат!\nСегодня я расскажу о своих любимых книгах.\n", sep='')

def ask_yes():
    answer = input("Готовы узнать?\n")
    answer = answer.lower()
    answer_flag = 0
    while answer_flag == 0:
        if answer.lower() == "да":
            print("Класс!\n")
            answer_flag = 2
            return 1
        elif answer.lower() == "нет":
            print(NewUser.name, ", душнилы ответ!", sep='')
            time.sleep(2)
            answer_flag = 1
            webbrowser.open("https://youtu.be/dQw4w9WgXcQ")
            exit()
            return 0
        else:
            answer = input("Напиши 'Да' или 'Нет'\n ")
            answer = answer.lower()
            
        
if ask_yes() == 1:
	print("Я люблю следующие жанры:\nАнтиутопия - напиши 'а'\nБизнес - 'б'\nКлассика - 'к'\nНаучпоп - 'н'\nПосмодернизм - 'п'\nЕсли хотите все книги - напишите 'в'\n")

cmd = ('а', 'б', 'в', 'к', 'н', 'п', ) 

url_book = ["https://youtu.be/dQw4w9WgXcQ","https://ru.m.wikipedia.org/wiki/1984_(%D1%80%D0%BE%D0%BC%D0%B0%D0%BD)", "https://ru.m.wikipedia.org/wiki/%D0%9E_%D0%B4%D0%B8%D0%B2%D0%BD%D1%8B%D0%B9_%D0%BD%D0%BE%D0%B2%D1%8B%D0%B9_%D0%BC%D0%B8%D1%80","https://ru.m.wikipedia.org/wiki/%D0%9C%D1%8B_(%D1%80%D0%BE%D0%BC%D0%B0%D0%BD)", "https://ru.m.wikipedia.org/wiki/451_%D0%B3%D1%80%D0%B0%D0%B4%D1%83%D1%81_%D0%BF%D0%BE_%D0%A4%D0%B0%D1%80%D0%B5%D0%BD%D0%B3%D0%B5%D0%B9%D1%82%D1%83#:~:text=Fahrenheit%20451)%20%E2%80%94%20%D0%BD%D0%B0%D1%83%D1%87%D0%BD%D0%BE%2D%D1%84%D0%B0%D0%BD%D1%82%D0%B0%D1%81%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9,%D0%9C%D0%BE%D0%BD%D1%82%D1%8D%D0%B3%2C%20%D1%81%D0%B6%D0%B8%D0%B3%D0%B0%D1%8E%D1%82%20%D0%BB%D1%8E%D0%B1%D1%8B%D0%B5%20%D0%BD%D0%B0%D0%B9%D0%B4%D0%B5%D0%BD%D0%BD%D1%8B%D0%B5%20%D0%BA%D0%BD%D0%B8%D0%B3%D0%B8.", "https://ru.m.wikipedia.org/wiki/%D0%A1%D0%BA%D0%BE%D1%82%D0%BD%D1%8B%D0%B9_%D0%B4%D0%B2%D0%BE%D1%80"]
answer = input("Какой жанр хотите?\n")
answer = answer.lower()

while answer not in cmd:
    print("Неверная команда, ", NewUser.name, ", попробуйте еще раз!", sep='')
    answer = input("Какой жанр хотите?\n")
    answer = answer.lower()

def define_book(url_book):
    yes_flag = 0
    print("Я могу подробнее рассказать о какой-то книге!")
    if ask_yes() == 1:
        num_book = input("О какой книге хотите узнать?\n")
        if num_book.isdigit() == True:
            num_book = int(num_book)
            if num_book > 0 and num_book < 6:
                url_book[num_book - 1].run_info()
            else:
    	        print("Такой книги нет, но может быть вы хотели увидеть вот это!\n")
    	        webbrowser.open_new("https://youtu.be/dQw4w9WgXcQ")
    return 0
    
#Антиутопия
if answer == 'а':
    Dystopia = Zhanr("Антиутопия", "5")
    a1 = Dystopia.Book("1984", "Оруэлл", "1", "https://ru.m.wikipedia.org/wiki/1984_(%D1%80%D0%BE%D0%BC%D0%B0%D0%BD)")
    a2 = Dystopia.Book("О дивный новый мир", "Хаксли", "2", "https://ru.m.wikipedia.org/wiki/%D0%9E_%D0%B4%D0%B8%D0%B2%D0%BD%D1%8B%D0%B9_%D0%BD%D0%BE%D0%B2%D1%8B%D0%B9_%D0%BC%D0%B8%D1%80")
    a3 = Dystopia.Book("Мы", "Замятин", "3", "https://ru.m.wikipedia.org/wiki/%D0%9C%D1%8B_(%D1%80%D0%BE%D0%BC%D0%B0%D0%BD)")
    a4 = Dystopia.Book("451 градус по Фаренгейту", "Брэдбери", "4", "https://ru.m.wikipedia.org/wiki/451_%D0%B3%D1%80%D0%B0%D0%B4%D1%83%D1%81_%D0%BF%D0%BE_%D0%A4%D0%B0%D1%80%D0%B5%D0%BD%D0%B3%D0%B5%D0%B9%D1%82%D1%83#:~:text=Fahrenheit%20451)%20%E2%80%94%20%D0%BD%D0%B0%D1%83%D1%87%D0%BD%D0%BE%2D%D1%84%D0%B0%D0%BD%D1%82%D0%B0%D1%81%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9,%D0%9C%D0%BE%D0%BD%D1%82%D1%8D%D0%B3%2C%20%D1%81%D0%B6%D0%B8%D0%B3%D0%B0%D1%8E%D1%82%20%D0%BB%D1%8E%D0%B1%D1%8B%D0%B5%20%D0%BD%D0%B0%D0%B9%D0%B4%D0%B5%D0%BD%D0%BD%D1%8B%D0%B5%20%D0%BA%D0%BD%D0%B8%D0%B3%D0%B8.")
    a5 = Dystopia.Book("Скотный двор", "Оруэлл", "5", "https://ru.m.wikipedia.org/wiki/%D0%A1%D0%BA%D0%BE%D1%82%D0%BD%D1%8B%D0%B9_%D0%B4%D0%B2%D0%BE%D1%80")
    print("Антиутопия, мой топ:")
    dystopias = [a1, a2, a3, a4, a5]
    i = 0
    while i < int(Dystopia.count):
        dystopias[i].print_info()
        i += 1
    define_book(dystopias)
    
#Бизнес-литература
if answer == 'б':
    Business = Zhanr("Бизнес-литература", "5")
    b1 = Business.Book("Кто украл мой сыр?", "Джонсон", "1", "https://en.m.wikipedia.org/wiki/Who_Moved_My_Cheese%3F")
    b2 = Business.Book("Камасутра для оратора", "Гандапас", "2", "https://www.litres.ru/radislav-gandapas/kamasutra-dlya-oratora-desyat-glav-o-tom-kak-poluchat-i/" )
    b3 = Business.Book("Дао Toyota: 14 принципов менеджмента ведущей компании мира", "Лайкер", "3", "https://www.google.com/url?sa=t&source=web&rct=j&url=https://www.ozon.ru/product/dao-toyota-14-printsipov-menedzhmenta-layker-dzheffri-254614930/%3Fsh%3DPAoOHXK1LQ&ved=2ahUKEwjFjsH-vK_5AhXmsosKHb-9AE8QFnoECA0QAQ&usg=AOvVaw3X1PVtWhQ2lkkCh13qhTAW")
    b4 = Business.Book("И ботаники делают бизнес", "Котляров", "4", "https://www.google.com/url?sa=t&source=web&rct=j&url=https://www.litres.ru/maksim-kotin/i-botaniki-delaut-biznes-1-2/&ved=2ahUKEwjimd6uva_5AhWRzYsKHS4DCsMQFnoECD4QAQ&usg=AOvVaw1XTTYNaVzBLFB6hYMlXrUW")
    b5 = Business.Book("Продавец обуви", "Найт", "5", "https://www.google.com/url?sa=t&source=web&rct=j&url=https://www.litres.ru/fil-nayt/prodavec-obuvi-istoriya-kompanii-nike-rasskazannaya-ee-osnovatele/otzivi/&ved=2ahUKEwiorK7Xva_5AhXm-yoKHUY3Ak8QFnoECDAQAQ&usg=AOvVaw36rxmUjFhhyfJsionPW3Cr")
    print("Бизнес-литература, мой топ:")
    business = [b1, b2, b3, b4, b5]
    i = 0
    while i < int(Business.count):
        business[i].print_info()
        i += 1
    define_book(business)
    
#Классика
if answer == 'к':
    Classic = Zhanr("Классика", "5")
    c1 = Classic.Book("Мастер и Маргарита", "Булгаков", "1", "https://www.google.com/url?sa=t&source=web&rct=j&url=https://ru.m.wikipedia.org/wiki/%25D0%259C%25D0%25B0%25D1%2581%25D1%2582%25D0%25B5%25D1%2580_%25D0%25B8_%25D0%259C%25D0%25B0%25D1%2580%25D0%25B3%25D0%25B0%25D1%2580%25D0%25B8%25D1%2582%25D0%25B0&ved=2ahUKEwj1qoL1wq_5AhUp-yoKHWxuAwUQmhN6BAgMEAI&usg=AOvVaw1U0znT65EDD1826ZJxUwII")
    c2 = Classic.Book("Шинель", "Гоголь", "2", "https://www.google.com/url?sa=t&source=web&rct=j&url=https://ru.m.wikipedia.org/wiki/%25D0%25A8%25D0%25B8%25D0%25BD%25D0%25B5%25D0%25BB%25D1%258C_(%25D0%25BF%25D0%25BE%25D0%25B2%25D0%25B5%25D1%2581%25D1%2582%25D1%258C)&ved=2ahUKEwjSpNmWw6_5AhWymIsKHY_6DnYQmhN6BAgKEAI&usg=AOvVaw3_mucdNYT7wlGJTeXEIOHG")
    c3 = Classic.Book("Робинзон Крузо", "Дефо", "3", "https://www.google.com/url?sa=t&source=web&rct=j&url=https://ru.m.wikipedia.org/wiki/%25D0%25A0%25D0%25BE%25D0%25B1%25D0%25B8%25D0%25BD%25D0%25B7%25D0%25BE%25D0%25BD_%25D0%259A%25D1%2580%25D1%2583%25D0%25B7%25D0%25BE&ved=2ahUKEwjj497Dw6_5AhWEk4sKHVlhDJMQmhN6BAgYEAI&usg=AOvVaw2g0xBYnDtlAHNTMIyVLP8H")
    c4 = Classic.Book("Капитанская дочка", "Пушкин", "4", "https://www.google.com/url?sa=t&source=web&rct=j&url=https://ru.m.wikipedia.org/wiki/%25D0%259A%25D0%25B0%25D0%25BF%25D0%25B8%25D1%2582%25D0%25B0%25D0%25BD%25D1%2581%25D0%25BA%25D0%25B0%25D1%258F_%25D0%25B4%25D0%25BE%25D1%2587%25D0%25BA%25D0%25B0&ved=2ahUKEwiMhtDmw6_5AhW0AxAIHR3GAfwQmhN6BAgREAI&usg=AOvVaw3MiEZtvaLyIcbteYTTDnXJ")
    c5 = Classic.Book("Евгений Онегин", "Пушкин", "5", "https://www.google.com/url?sa=t&source=web&rct=j&url=https://ru.m.wikipedia.org/wiki/%25D0%2595%25D0%25B2%25D0%25B3%25D0%25B5%25D0%25BD%25D0%25B8%25D0%25B9_%25D0%259E%25D0%25BD%25D0%25B5%25D0%25B3%25D0%25B8%25D0%25BD&ved=2ahUKEwj0iZmGxK_5AhXomIsKHZsgDAEQFnoECD0QAQ&usg=AOvVaw1orBIJOuf4Urvi5B_7spjG")
    print("Классика, мой топ:")
    classic = [c1, c2, c3, c4, c5]
    i = 0
    while i < int(Classic.count):
        classic[i].print_info()
        i += 1
    define_book(classic)
#Научпоп
if answer == 'н':
    Science = Zhanr("Научпоп", 5)
    s1 = Science.Book("Эгоистичный ген", "Докинз", "1", "https://www.google.com/url?sa=t&source=web&rct=j&url=https://ru.m.wikipedia.org/wiki/%25D0%25AD%25D0%25B3%25D0%25BE%25D0%25B8%25D1%2581%25D1%2582%25D0%25B8%25D1%2587%25D0%25BD%25D1%258B%25D0%25B9_%25D0%25B3%25D0%25B5%25D0%25BD&ved=2ahUKEwjSt_7uy6_5AhVKCBAIHbJiBdAQmhN6BAgKEAI&usg=AOvVaw1Sut7-5UmEZCnc6zLWYmjx")
    s2 = Science.Book("Гармоны счастья", "Бройнинг", "2", "https://www.google.com/url?sa=t&source=web&rct=j&url=https://ru.m.wikipedia.org/wiki/%25D0%2593%25D0%25BE%25D1%2580%25D0%25BC%25D0%25BE%25D0%25BD%25D1%258B_%25D1%2581%25D1%2587%25D0%25B0%25D1%2581%25D1%2582%25D1%258C%25D1%258F&ved=2ahUKEwj3xs-e0q_5AhUS6CoKHdxjD98QmhN6BAgKEAI&usg=AOvVaw0odtrogsW9gaC3zzycjmJO")
    s3 = Science.Book("Голая статистика", "Уилан", "3", "https://www.google.com/url?sa=t&source=web&rct=j&url=https://www.litres.ru/charlz-uilan/golaya-statistika-samaya-interesnaya-kniga-o-samoy-skuchnoy-n/otzivi/&ved=2ahUKEwic2szD0q_5AhXUAxAIHfa9CJcQFnoECBQQAQ&usg=AOvVaw3V8ikVaf6vQd1VCLXTK4ey")
    s4 = Science.Book("Человек, который принял жену за шляпу", "Сакс", "4", "https://www.google.com/url?sa=t&source=web&rct=j&url=https://ru.m.wikipedia.org/wiki/%25D0%25A7%25D0%25B5%25D0%25BB%25D0%25BE%25D0%25B2%25D0%25B5%25D0%25BA,_%25D0%25BA%25D0%25BE%25D1%2582%25D0%25BE%25D1%2580%25D1%258B%25D0%25B9_%25D0%25BF%25D1%2580%25D0%25B8%25D0%25BD%25D1%258F%25D0%25BB_%25D0%25B6%25D0%25B5%25D0%25BD%25D1%2583_%25D0%25B7%25D0%25B0_%25D1%2588%25D0%25BB%25D1%258F%25D0%25BF%25D1%2583%23:~:text%3D%25C2%25AB%25D0%25A7%25D0%25B5%25D0%25BB%25D0%25BE%25D0%25B2%25D0%25B5%25D0%25BA%252C%2520%25D0%25BA%25D0%25BE%25D1%2582%25D0%25BE%25D1%2580%25D1%258B%25D0%25B9%2520%25D0%25BF%25D1%2580%25D0%25B8%25D0%25BD%25D1%258F%25D0%25BB%2520%25D0%25B6%25D0%25B5%25D0%25BD%25D1%2583%2520%25D0%25B7%25D0%25B0,%25D0%25A1%25D0%25B0%25D0%25BA%25D1%2581%25D0%25B0%252C%2520%25D0%25B0%25D0%25B2%25D1%2582%25D0%25BE%25D1%2580%25D0%25B0%2520%25C2%25AB%25D0%259F%25D1%2580%25D0%25BE%25D0%25B1%25D1%2583%25D0%25B6%25D0%25B4%25D0%25B5%25D0%25BD%25D0%25B8%25D1%258F%25C2%25BB.&ved=2ahUKEwi1w_Lq0q_5AhUsposKHQ4TARsQFnoECAsQBQ&usg=AOvVaw3897Hu-WY8dijpATWLO69j")
    s5 = Science.Book("Красная таблетка", "Курпатов", "5", "https://www.google.com/url?sa=t&source=web&rct=j&url=https://www.litres.ru/andrey-kurpatov/krasnaya-tabletka-posmotri-pravde-v-glaza/chitat-onlayn/&ved=2ahUKEwil0eOK06_5AhVuw4sKHVV0A4oQFnoECEgQAQ&usg=AOvVaw1C2VeWgASAJXEK6feYwgko")
    print("Научпоп, мой топ:")
    science = [s1, s2, s3, s4, s5]
    i = 0
    while i < int(Science.count):
        science[i].print_info()
        i += 1
    define_book(science)
#Постмодернизм
if answer == 'п':
    Postmodern = Zhanr("Постмодернизм", "5")
    p1 = Postmodern.Book("IPhuck 10", "Пелевин", "1", "https://www.google.com/url?sa=t&source=web&rct=j&url=https://ru.m.wikipedia.org/wiki/IPhuck_10&ved=2ahUKEwiNl5-T1K_5AhURiIsKHcYIAXwQmhN6BAgKEAI&usg=AOvVaw0nM7FwSgsaLidI-63lMC6I")
    p2 = Postmodern.Book("Любовь к трем цукербринам", "Пелевин", "2", "https://www.google.com/url?sa=t&source=web&rct=j&url=https://ru.m.wikipedia.org/wiki/%25D0%259B%25D1%258E%25D0%25B1%25D0%25BE%25D0%25B2%25D1%258C_%25D0%25BA_%25D1%2582%25D1%2580%25D1%2591%25D0%25BC_%25D1%2586%25D1%2583%25D0%25BA%25D0%25B5%25D1%2580%25D0%25B1%25D1%2580%25D0%25B8%25D0%25BD%25D0%25B0%25D0%25BC&ved=2ahUKEwizxI-41K_5AhWHjYsKHXWYDj0QmhN6BAgLEAI&usg=AOvVaw2MRGqr1A020qM063jGspGo")
    p3 = Postmodern.Book("Чапаев и пустота", "Пелевин", "3", "https://www.google.com/url?sa=t&source=web&rct=j&url=https://ru.m.wikipedia.org/wiki/%25D0%25A7%25D0%25B0%25D0%25BF%25D0%25B0%25D0%25B5%25D0%25B2_%25D0%25B8_%25D0%259F%25D1%2583%25D1%2581%25D1%2582%25D0%25BE%25D1%2582%25D0%25B0&ved=2ahUKEwi97p7h1K_5AhUR_SoKHZq3BaIQmhN6BAgKEAI&usg=AOvVaw3yu3mkr7VWHde2gsClmfE7")
    p4 = Postmodern.Book("Т", "Пелевин", "4", "https://www.google.com/url?sa=t&source=web&rct=j&url=https://ru.m.wikipedia.org/wiki/T_(%25D1%2580%25D0%25BE%25D0%25BC%25D0%25B0%25D0%25BD)&ved=2ahUKEwjArKP81K_5AhVxx4sKHcBGB3QQmhN6BAgLEAI&usg=AOvVaw1BAnPuxUl8DdwTjkChAUhF")
    p5 = Postmodern.Book("Смотритель", "Пелевин", "5", "https://www.google.com/url?sa=t&source=web&rct=j&url=https://ru.m.wikipedia.org/wiki/%25D0%25A1%25D0%25BC%25D0%25BE%25D1%2582%25D1%2580%25D0%25B8%25D1%2582%25D0%25B5%25D0%25BB%25D1%258C_(%25D1%2580%25D0%25BE%25D0%25BC%25D0%25B0%25D0%25BD)&ved=2ahUKEwjLvKma1a_5AhXhpYsKHaRTBWQQmhN6BAgHEAI&usg=AOvVaw3yMfKKVJ3VoRviSp3GFqul")
    print("Постмодернизм, мой топ:")
    postmodern = [p1, p2, p3, p4, p5]
    i = 0
    while i < int(Postmodern.count):
        postmodern[i].print_info()
        i += 1
    define_book(postmodern)
    
#Все жанры
if answer == 'в':
	print("Антиутопия, мой топ:\n1. 1984 - Оруэлл\n2. О дивный новый мир - Хаксли\n3. Мы - Замятин\n4. 451 градус по Фаренгейту - Брэдбери\n5. Скотный двор - Оруэлл\n")
	print("Бизнес, мой топ:\n1. Кто украл мой сыр? - Джонсон\n2. Камасутра для оратора - Гандапас\n3. Дао Toyota: 14 принципов менеджмента ведущей компании мира - Лайкер\n4. И ботаники делают бизнес - Котляров\n5. Продавец обуви - Найт\n")
	print("Классика, мой топ:\n1. Мастер и Маргарита - Булгаков\n2. Шинель - Гоголь\n3. Робинзон Крузо - Дефо\n4. Капитанская дочка - Пушкин\n5. Евгений Онегин - Пушкин\n")
	print("Научпоп, мой топ:\n1. Эгоистичный ген  - Докинз\n2. Гармоны счастья - Бройнинг\n3. Голая статистика - Уилан\n4. Человек, который принял жену за шляпу - Сакс\n5. Красная Таблетка - Курпатов\n")
	print("Постмодернизм, мой топ:\n1. IPhuck 10 - Пелевин\n2. Любовь к трем Цукербринам - Пелевин\n3. Чапаев и пустота - Пелевин\n4. 'T' - Пелевин\n5. Смотритель - Пелевин\n")

print("Есть книги, которые я не читал, но хотел бы")
if ask_yes() == 1:
	r1 = Recommend("Transhumanism inc", "Пелевин")
	r2 = Recommend("Хлеб с ветчиной", "Буковски")
	r3 = Recommend("Судьба человека", "Шолохов")
	recommend = [r1, r2, r3]
	for element in recommend:
		element.get_name()
		element.get_author()

print("Был рад повидаться, ", NewUser.name,", заходи ещё!", sep='')
	
