# На вход программе подается строка текста. Если в этой строке буква «f» встречается только один раз, выведите её индекс. Если она встречается два и более раз, выведите индекс её первого и последнего вхождения на одной строке, разделенных символом пробела. Если буква «f» в данной строке не встречается, следует вывести «NO».

txt = input()
if txt.count("f") == 1:
  print(txt.find("f"))
elif txt.count("f") == 0:
  print("NO")
else:
  print(txt.find("f"), txt.rfind("f"))
