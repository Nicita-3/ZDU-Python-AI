import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    confusion_matrix,
    classification_report,
    accuracy_score
)
from sklearn.model_selection import train_test_split

df = pd.read_csv("lab-7/data.csv")
df = df.drop(columns=["Unnamed: 32"])
df = df.drop(columns=["id"])

df["diagnosis"] = df["diagnosis"].map({"M": 1, "B": 0})

x = df.drop(columns=["diagnosis"]) # Тут все крім діагноза
y = df["diagnosis"]

X_train, X_test, y_train, y_test = train_test_split(
    x, y, test_size=0.25, random_state=6
)

scaler = StandardScaler().fit(X_train)

X_train_scaled = scaler.transform(X_train)
X_test_scaled  = scaler.transform(X_test)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)

print("\nМатриця помилок:")
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred, target_names=["B (0)", "M (1)"])) # B - н, M - п, 

print("Точність:", accuracy_score(y_test, y_pred))

# [ПН НП]
# [НН ПП]