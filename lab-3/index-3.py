# Напишіть функцію,
# яка генерує всі можливі підмножини заданої множини символів
# без врахування перестановок та вивести їх на екран.

# s = input("Введіть рядок символів: ")
# subsets = set()
# n = len(s)

# for i in range(2**n):
#     subset = ''
#     for j in range(n):
#         if (i & (1 << j)) > 0:
#             subset += s[j]
#     subsets.add(subset)

# result = sorted(subsets, key=lambda x: (len(x), x))

# for subset in result:
#     print(f"'{subset}'")

s = "abc"
n = len(s)

for i in range(2**n):
    subset = ''
    print(f"i = {i:0{n}b}  (десяткове {i})")
    for j in range(n):
        mask = 1 << j
        print(f"   j = {j}, маска = {mask:0{n}b}, i ({i:0{n}b}) & маска ({mask:0{n}b}) = {i & mask}")
        if (i & mask) > 0:
            subset += s[j]
            print(f"      → додаємо s[{j}] = '{s[j]}'")
    print(f"Підмножина: '{subset}'\n")

