# coding=utf-8

abc = {'q': 'й', 'w': 'ц', 'e': 'у', 'r': 'к', 't': 'е', 'y': 'н', 'u': 'г', 'i': 'ш',
       'o': 'щ', 'p': 'з', '[': 'х', ']': 'ъ', 'a': 'ф', 's': 'ы', 'd': 'в', 'f': 'а',
       'g': 'п', 'h': 'р', 'j': 'о', 'k': 'л', 'l': 'д', '\'': 'э', 'z': 'я', 'x': 'ч',
       'c': 'с', 'v': 'м', 'b': 'и', 'n': 'т', 'm': 'ь', ',': 'б', '.': 'ю', ';': 'ж',
       'Q': 'Й', 'W': 'Ц', 'E': 'У', 'R': 'К', 'T': 'Е', 'Y': 'Н', 'U': 'Г', 'I': 'Ш',
       'O': 'Щ', 'P': 'З', '{': 'Х', '}': 'Ъ', 'A': 'Ф', 'S': 'Ы', 'D': 'В', 'F': 'А',
       'G': 'П', 'H': 'Р', 'J': 'О', 'K': 'Л', 'L': 'Д', '\"': 'Э', 'Z': 'Я', 'X': 'Ч',
       'C': 'С', 'V': 'М', 'B': 'И', 'N': 'Т', 'M': 'Ь', '<': 'Б', '>': 'Ю', ':': 'Ж',
       '?': '?', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7',
       '8': '8', '9': '9', '0': '0', ' ': ' ', '!': '!', '-': '-', '_': '_', '+': '+',
       '=': '=', '(': '(', ')': ')'}

slovo = str(input('Введите текст: '))
new_slovo = []
for bu in slovo:
    for key in abc:
        if bu == key:
            new_slovo.append(abc[key])
new_slovo = ''.join(new_slovo)
print(new_slovo)
