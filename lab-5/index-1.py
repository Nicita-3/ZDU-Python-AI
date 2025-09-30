# Pclass — клас пасажира (1 — високий, 2 — средній, 3 — низький);
# Name — ім’я;
# Sex — стать;
# Age — вік;
# SibSp — кількість братів, сестер на борту корабля;
# Parch — кількість батьків, дітей на борту корабля;
# Ticket — номер білета;
# Fare — оплата;
# Cabin — номер каюти;
# Embarked — порт (C — Шербур; Q — Квінстаун; S —
# Саутгемптон)

# СТорінка 47 https://eprints.zu.edu.ua/40845/1/PraktykumAI.pdf?authuser=0
# 1)Виведіть загальну інформацію про зазначену базу даних.
# 2)Виведіть перші 5 та останні 10 записів.
# 3)Виведіть тільки тих хто не вижив після катастрофи та збережіть
# інформацію у окремий DataFrame.
# 4)До яких класів білетів переважно належали ці люди.
# 5)Побудуйте стовпчасту діаграму, яка показувала кількість дітей,
# підлітків, молодих людей, людей працездатного віку та пенсійного віку,
# що не вижили після трагедії.

import pandas as pd
import matplotlib.pyplot as plt

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"

db = pd.read_csv("lab-5/titanic.csv")

print(RED + "<<<===>>> Загальна інформація <<<===>>>" + RESET)
print(db.info())

print(RED + "\n<<<===>>> Перші 5 записів <<<===>>>" + RESET)
print(db.head(5))

print(RED + "\n<<<===>>> Останні 10 записів <<<===>>>" + RESET)
print(db.tail(10))

not_survived = db[db["Survived"] == 0]
print(RED + "\n<<<===>>> Пасажири, які не вижили <<<===>>>" + RESET)
print(not_survived.head())
df_not_survived = not_survived.copy()

print(YELLOW + "\n<<<===>>> Розподіл за класами серед тих, хто не вижив <<<===>>>" + RESET)
print(df_not_survived["Pclass"].value_counts())

def age_group(age):
    if pd.isna(age):
        return "Невідомо"
    elif age < 12:
        return "Діти"
    elif age < 18:
        return "Підлітки"
    elif age < 35:
        return "Молодь"
    elif age < 60:
        return "Працездатні"
    else:
        return "Пенсіонери"

df_not_survived["AgeGroup"] = df_not_survived["Age"].apply(age_group)

age_counts = df_not_survived["AgeGroup"].value_counts()

print(GREEN + "\n<<<===>>> Розподіл за віковими групами серед тих, хто не вижив <<<===>>>" + RESET)
print(age_counts)

plt.figure(figsize=(8,5))
age_counts.plot(kind="bar", color="red")
plt.title("Кількість людей різних вікових груп, які не вижили")
plt.xlabel("Вікова група")
plt.ylabel("Кількість")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
