# coding=utf-8
import slovar


slo = slovar.abc
while True:
    slovo = str(input('Введите текст: '))
    new_slovo = []
    for bu in slovo:
        for key in slo:
            if bu == key:
                new_slovo.append(slo[key])
    new_slovo = ''.join(new_slovo)
    if new_slovo == '':
        break
    print(new_slovo+"\n")
