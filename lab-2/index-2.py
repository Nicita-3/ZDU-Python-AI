# Цілі числа вводяться через пропуск у один рядок.
# Трансформуйте цей рядок чисел у двовимірний список.
# Забезпечте коректність введення даних.
# Забезпечте коректність введення даних у двовимірний список.
# Перевірте, чи заданий двовимірний список цілих має горизонтальну вісь симетрії.
print("Введіть розмір масиву m x n")
m = int(input("Введіть m: "))
n = int(input("Введіть n: "))
numbers = []
str = input(f"Введіть масив {m}x{n} ({m*n}): ")
try:
    numbersR = [int(x) for x in str.split()]
    numbersN = [[] for _ in range(m)]
    if len(numbersR) != m*n:
        print(f"Ви ввели {len(numbersR)} чисел замість {m*n}. Спробуйте ще раз.")
        exit()
    for i in range(0, m*n, n):
        j = i // n
        numbersN[j] = numbersR[i : i+n]
        if len(numbersN[j]) != n:
            print(f"Ви ввели {len(numbersN[i])} чисел замість {n}. Спробуйте ще раз.")
            exit()
except ValueError:
    print("Некоректний ввід. Будь ласка, введіть лише цілі числа")
    exit()
numbers = numbersN
if (numbers == numbers[::-1]):
    print("Список має горизонтальну вісь симетрії")
else:
    print("Список не має горизонтальну вісь симетрії")