# 1) Розмістіть на Вашому Google Disk файл бази даних з
# інформацією про дослідження.
# 2) Адаптуйте дані, щоб було можливим створити найбільш
# ефективну алгоритм кластеризації (відповідно до Вашого
# варіанта).
# 3) Виконайте кластеризацію даних.
# 4) Кожен окремий кластер збережіть у окремий dataFrame.
# 5) Побудуйте точкову діаграму, яка відображатиме виокремлені
# кластери кольором та міститиме легенду діаграми, що
# позначатиме кожен кластер.
# 6) Зробіть висновки про ефективність створеної моделі.

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import MeanShift

df = pd.read_csv("lab-8/Lab_08_Var_02.csv")
X = df[['x', 'y']]

model = MeanShift(bandwidth = 8)
df['cluster'] = model.fit_predict(X)

clusters = []
for i in range(len(model.cluster_centers_)):
    cluster_df = df[df['cluster'] == i]
    clusters.append(cluster_df)
    cluster_df.to_csv(f"lab-8/cls/cluster_{i}.csv", index=False)

plt.figure(figsize=(7, 5))

for i in range(len(model.cluster_centers_)):
    plt.scatter(
        clusters[i]['x'],
        clusters[i]['y'],
        label=f'Кластер {i}'
    )

plt.xlabel("x")
plt.ylabel("y")
plt.title("KMeans кластери (x, y)")
plt.legend()
plt.grid(True)
plt.show()