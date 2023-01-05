# Проекты на Python

### 
> *Путеводитель.*
* [**Карманный переводчик с английского**](https://github.com/i-galimov/python/blob/main/projects/translate/lite_tutor_english1.0.py)
* [**Парсер с Пикабу**](https://github.com/i-galimov/python/blob/main/projects/parser/parser-pikabu.py)
* [**Боты в Телеграм**](https://github.com/i-galimov/python/tree/main/projects/Python_bot)
* [**Какую книжку почитать?**](https://github.com/i-galimov/python/blob/main/projects/books/my_favorite_books.py)
* [**Русская рулетка**](https://github.com/i-galimov/python/blob/main/projects/roulette/roulette.py)
---
### [Пример кода](https://github.com/i-galimov/python/blob/main/projects/shuffle/shuffle_str.py) 
> *Это не баг, а фича*
```
import shutil
import random

name_file = input("Введите название файла, который нужно перемешать\n")
try:
    c = open("shuffle.txt", "x")
except:
    print('Файл "shuffle.txt" уже существует!')
    
encoding = [
'utf-8',
'windows-1252',
'utf-16',
'GBK',
'ASCII',
'US-ASCII',
'Big5',
'cp500'
]
correct_encoding = ''
for enc in encoding:
    try:
        open(name_file, encoding=enc).read()
    except (UnicodeDecodeError, LookupError):
        pass
    else:
        correct_encoding = enc
        break
print("Кодировка файла -", correct_encoding)

shutil.copy(name_file, "shuffle.txt", follow_symlinks=True)
f = open("shuffle.txt", encoding=correct_encoding) 
x = f.readlines() 
f.close()
random.shuffle(x)
f = open("shuffle.txt", "w")
f.writelines(x)
f.close()
print("Файл ", name_file, " перемешан! Результат хранится в файле shuffle.txt", sep='')
```
********
