# 2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в
# последовательность кодов (не используя методы encode и decode ) и определить тип,
# содержимое и длину соответствующих переменных.

words = []
words.append(b"class")
words.append(b"function")
words.append(b"method")

for word in words:
    print(word)
    print(type(word))
    print(len(word))
