from bs4 import BeautifulSoup
import requests
import sys

f = open("pikabu.txt", 'w')
f.write("В этом файле результаты поиска по тегам Пикабу.\n")
f.close()

search_words = input('Что хотите найти на Пикабу?\n') 
limit_page = int(input("Сколько страниц пролистать?\n"))
search_words_plus = search_words.replace(' ', '+')
user_agent = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/89.0.4389.72 Safari/537.36'}
if limit_page < 1:
	sys.exit("Неверное число страниц поиска")
	
for i in range(1, limit_page + 1):
	if requests.get('https://pikabu.ru/tag/' + search_words, params={'st': 3, 't': search_words_plus, 'page': i}, headers=user_agent).status_code == 200:
		parsed_pikabu = BeautifulSoup(requests.get('https://pikabu.ru/tag/' + search_words, params={'st': 3, 't': search_words_plus, 'page': i}, headers=user_agent).text, "html.parser")
		text = parsed_pikabu.select('.story-block_type_text')
		print("Ищем на странице, номер: ", i)
		for el in text:
			f = open("pikabu.txt", 'a')
			str_spam = str(el)
			if str_spam.find("from=cpm") != -1 or str_spam.find("href") != -1 or str_spam.find("***") != -1 or str_spam.find("еклама") != -1 or str_spam.find("...") != -1:
				continue
			str1 = el.get_text()
			if len(str1) < 20 or "акция" in str1 or "подарок" in str1 or "купить" in str1 or "скидки" in str1 or "наушник" in str1 or "сертификат" in str1:
				continue
			f.write(str1)
			f.close()
	if requests.get('https://pikabu.ru/tag/' + search_words, {'st': 3, 't': search_words_plus, 'page': i}, headers=user_agent).status_code != 200:
		print("Сервер вернул код ошибки: ", requests.get('https://pikabu.ru/tag/' + search_words, params={'st': 3, 't': search_words_plus, 'page': i}, headers=user_agent).status_code)

def delete_string():
    File = open("pikabu.txt", 'r')
    str_list = []
    for i in File.readlines():
        if i not in str_list:
            str_list.append(i)
    File.close()
    File = open("pikabu.txt", 'w')
    for j in str_list:
        File.write(j + '\n')

delete_string()
print('Записано в файл "pikabu.txt"')
print("Поиск завершился")
