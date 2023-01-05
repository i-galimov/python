# Напишите программу, выводящую следующий список:

# ['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]

spis = []
for i in range(26):
  a = i + 1
  spis.append(chr(97+i)*a)
print(spis)
