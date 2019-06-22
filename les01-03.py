# 3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в
# байтовом типе.

words = []
words.append(b"attribute")  # возможно
words.append(b"класс")      # невозможно записать SyntaxError: bytes can only contain ASCII literal characters.
words.append(b"функция")    # невозможно записать SyntaxError: bytes can only contain ASCII literal characters.
words.append(b"type")       # возможно

for word in words:
    print(word)
    print(type(word))
    print(len(word))