import random

verb_dict = {'ask': ('спрашивать', 'просить'), 'become': 'становиться', 'begin':
'начинать', 'call': ('кричать', 'звать', 'звонить'), 'can':
('мочь', 'быть в состоянии'), 'come':
('приходить', 'приезжать', 'заходить'), 'could': 'можете', 'do':
('делать', 'выполнять', 'создавать'), 'feel':
('чувствовать', 'считать'), 'find':
('находить', 'встречать', 'обнаруживать', 'заставать', 'считать', 'полагать', 'признавать'),
'get':
('получить', 'купить',
'понять', 'добраться'),
'give': ('давать', 'дарить'),
'go':
('идти', 'ехать'), 'have':
('иметь', 'быть вынужденным'), 'hear':
('слышать', 'слушать'),
'help': 'помогать',
'keep': ('держать', 'хранить', 'продолжать'), 'know':
('знать', 'понимать'), 'leave': ('оставлять', 'покидать', 'уезжать'), 'let': 
('разрешать', 'позволять'), 'like':
('любить', 'нравиться'), 'live':
('жить', 'обитать'),
'look':
('смотреть', 'осматривать', 'выглядеть', 'казаться'), 'make': ('делать', 'создавать',
'готовить'), 'may': ('возможно',
'можно'), 'mean':
('иметь в виду', 'подразумевать', 'значить',
'намереваться', 'хотеть что-либо сделать'), 'might':
('мог бы', 'может', 'можно ли'), 'move': ('двигать', 'двигаться', 'переезжать'),
'need':
('нуждаться', 'иметь необходимость'), 'play': 'играть',
'put':
('класть', 'ставить', 'помещать'),
'run': 
('бежать', 'бегать', 'управлять'),
'say': ('говорить', 'сказать'), 'see': ('видеть', 'смотреть', 'понимать', 'встречать', 'посещать'),
'seem': 'казаться',
'should':
('следует', 'должен быть'), 'show': 'показывать', 'start': 'начинать',
'take':
('брать', 'принимать',
'вмещать', 'требоваться'), 'talk': ('разговаривать', 'говорить', 'вести беседу'), 'tell':
('говорить', 'рассказывать', 'сообщать'),
'think': 'думать', 'try': 'пытаться, пробовать',
'turn':
('вращать', 'поворачивать', 'вывихивать', 'исполниться'), 'use': ('использовать', 'употреблять'), 'want':
('хотеть', 'желать', 'нуждаться'), 'work': 'работать', 'will':
('велеть', 'желать'), 'would': ('не могли бы', 'не желаете ли')}

len_all = len(verb_dict) # считаем, сколько слов в словаре

print(f'Всего в словаре {len_all} слов')

user_input = input('Введите слово или фразу на английском, которые хотите перевести, или цифры, чтобы сгенерировать случайную фразу\n')

check_type = user_input.isdigit()

# проверка на тип данных в вводе
if check_type == False:
	user_input = user_input.lower().split()
else:
	user_input = int(user_input)

# выводит перевод слов по отдельности, если нет в словаре пишет '?'
def fn_translate(user_input):
    count_not_dict = 0 # счетчик ненайденных слов
    count_dict = 0 # счетчик слов, найденных в словаре
    for element in user_input:
      if element in verb_dict:
      	print(element, verb_dict[element])
      	count_dict += 1
      elif element not in verb_dict:
      	print(element, "?")
      	count_not_dict += 1
    count_all_dict = count_dict + count_not_dict # всего слов ввел пользователь
    percent_dict = (count_dict / count_all_dict) * 100 # процент переведенных слов
  # статистика по переводу
    print(f'Всего использовано {count_all_dict} слов\nУдалось перевести {count_dict} слов\nНе удалось найти {count_not_dict} слов\nПереведено {percent_dict} процентов текста')

# вывод случайных слов из словаря, сколько захочет пользователь
def fn_random_word(user_input):
        if user_input > 50:
        	print("Слишком большое число, придумаем 50 слов")
        	user_input = 50
        while user_input > 0:
        	en_random = random.choice(list(verb_dict.keys()))
        	print(en_random)
        	user_input -= 1
		
if check_type == True:
	fn_random_word(user_input)
else:
	fn_translate(user_input)
