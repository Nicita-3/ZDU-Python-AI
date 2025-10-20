# 2) Адаптуйте дані до використання лінійної регресії.
# 3) Розділіть дані на тестову та навчальну вибірки.
# 4) Побудуйте модель машинного навчання, яка дозволяє
# прогнозувати вартість страхування в залежності від віку, індексу маси
# тіла та регіону, де людина проживає.
# 5) Порівняйте спрогнозовані результати із реальними даними.
# Знайдіть різницю між реальними даними тестової вибірки та
# прогнозованими, зокрема обчисліть, який відсоток становить абсолютне
# значення похибки до реальних даних.
# 6) Побудуйте гістограму відсоткових значень похибки для
# кожного прогнозованого результату.
# 7) Напишіть висновок про ефективність побудованої моделі.
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

df = pd.read_csv("./lab-6/insurance.csv")

required = set(["age", "bmi"] + ["expenses", "region"])
# вік (age), індекс маси тіла (bmi), регіон проживання (region), реальні витрати на страхування (expenses)

df = pd.get_dummies(df, columns=["region"], prefix="region", drop_first=False)

feature_cols = ["age", "bmi"] + [c for c in df.columns if c.startswith("region_")]
X = df[feature_cols].copy()
y = df["expenses"].copy()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

pct_error = (np.abs(y_pred - y_test) / (y_test.replace(0, np.nan))).abs() * 100

hist_data = pct_error.dropna()

plt.figure(figsize=(8, 5))
plt.hist(hist_data, bins=30)
plt.xlabel("Відсоткова абсолютна похибка (%)")
plt.ylabel("Кількість прикладів")
plt.title("Гістограма відсоткових значень похибки")
plt.tight_layout()
plt.show()
