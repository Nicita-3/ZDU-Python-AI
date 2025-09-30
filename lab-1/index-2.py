# 2. Вводиться ціле число n. Виведіть, чи є воно додатним, від'ємним
# або дорівнює 0. Виведіть «Positive», «Negative» чи «Zero» в залежності
# від значення n. [eolymp.com, задача № 8242]
n = int(input("n: "))
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")