# 1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и
# проверить тип и содержание соответствующих переменных. Затем с помощью
# онлайн-конвертера преобразовать строковые представление в формат Unicode и также
# проверить тип и содержимое переменных.

words = []
words.append("разработка")
words.append("сокет")
words.append("декоратор")
u_words = []
u_words.append("\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430")
u_words.append("\u0441\u043e\u043a\u0435\u0442")
u_words.append("\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440")

for word in words:
    print(word)
    print(type(word))

for u_word in u_words:
    print(u_word)
    print(type(u_word))