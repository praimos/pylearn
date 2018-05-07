# coding=utf-8
import slovar


slo = slovar.abc
slovo = str(input('Введите текст: '))
new_slovo = []
for bu in slovo:
    for key in slo:
        if bu == key:
            new_slovo.append(slo[key])
new_slovo = ''.join(new_slovo)
print(new_slovo)
