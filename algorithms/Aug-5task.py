# Пройдя тестовое задание от куратора из предыдущей задачи, вы получили новое. На этой раз вам нужно улучшить систему поиска карточек в бухгалтерии Тинькофф.
# Всего у нас работает ﻿﻿nn﻿﻿ людей. Каждый человек определяется своей фамилией, состоящей из строчных букв латинского алфавита ﻿﻿(a, ..., z)(a,...,z)﻿﻿. К сожалению, бумажные записи со временем становятся нечитаемыми, т.к. конец фамилии стирается, но команда бухгалтерии отлично знает систему хранения карточек и умеет находить любого сотрудника по префиксу его фамилии.
# Для более быстрой работы дополнительно требуется знать ﻿﻿kk﻿﻿-го в лексикографическом порядке человека среди всех с заданным префиксом. Задачу быстрого поиска такого человека и поставил перед вами куратор.
# Формат входных данных
# Первая строка задает два натуральных числа ﻿﻿nn﻿﻿ и ﻿﻿qq﻿﻿ ﻿﻿(1 \leq n \leq 10^6, 1 \leq q \leq 10^4)(1≤n≤106,1≤q≤104)﻿﻿ — количество людей и количество обращений к системе соответственно.
# В следующих ﻿﻿n﻿﻿ строках находятся фамилии, состоящие из строчных букв латинского алфавита. Гарантируется, что суммарная длина строк не превосходит ﻿﻿10^6106﻿﻿ символов.
# Последние ﻿﻿q﻿﻿ строк содержат запросы. Каждый запрос состоит из числа ﻿﻿k_iki​﻿﻿ и строки ﻿﻿s_isi​﻿﻿ ﻿﻿(1 \leq i \leq q, 1\leq k_i \leq 10^9, 1 \leq s_i \leq 10^3)(1≤i≤q,1≤ki​≤109,1≤si​≤103)﻿﻿, задающей префикс фамилии, среди которых нужно найти ﻿﻿k_iki​﻿﻿-ю по порядку строку.
# Формат выходных данных
# На каждый запрос выведите одно число — порядковый номер найденной фамилии в исходном наборе или ﻿﻿-1−1﻿﻿, если фамилии, подходящей под условие, не существует.

digits = input().split()
contacts = int(digits[0])
num_requests = int(digits[1])

last_names = [input() for i in range(contacts)]
last_names_sort = sorted(last_names)

requests = [input().split() for i in range(num_requests)]

i = 0
num_search = [0 for i in range(num_requests)]
value_search = ["0" for i in range(num_requests)]
while i < num_requests - 1:
	num_search[i] = int(requests[i][0])
	value_search[i] = requests[i][1]
	i += 1

i = 0
j = 0
while i < num_requests - 1:
	while num_search[j] > 0:
		if last_names_sort[i].find(value_search[j]) == 0:
			num_search[j] -= 1
		i += 1
	if num_search[j] == 0:
		print(i + 1)
	else:
		print("-1")
	i = 0
	j += 1
	
