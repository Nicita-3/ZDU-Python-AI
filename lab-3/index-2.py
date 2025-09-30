# Створіть функцію, яка визначає кількість слів у заданому рядку,
# використовуючи лише класичні інструкції мови Python,
# властивість length та доступ до символу через індекс.
str = input("Введіть рядок: ")
def count_words(s):
    count = 0
    in_word = False

    for i in range(len(s)):
        if s[i] != " " and not in_word:
            in_word = True
            count += 1
        elif s[i] == " ":
            in_word = False

    return count
print("Кількість слів у рядку:", count_words(str))