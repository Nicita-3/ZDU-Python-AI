# 2. Вивести список всіх дільників числа m (число вводиться
# користувачем з консолі).
m = int(input("m: "))
divisors = []
for i in range(1, m + 1):
    if m % i == 0:
        divisors.append(i)
print("Дільники числа", m, ":", divisors)