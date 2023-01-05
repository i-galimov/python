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
