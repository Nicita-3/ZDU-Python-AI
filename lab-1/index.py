# 2. Задано чотири точки паралелограма за допомогою координат
# його вершин. Визначити площу паралелограма та довжину його
# діагоналей. Результат округлити до тисячних.
# [1, 2], [4, 6], [7, 2], [4, -2]
import math
points = [[0, 0], [0, 0], [0, 0], [0, 0]]
points[0][0] = float(input("x1: "))
points[0][1] = float(input("y1: "))
points[1][0] = float(input("x2: "))
points[1][1] = float(input("y2: "))
points[2][0] = float(input("x3: "))
points[2][1] = float(input("y3: "))
points[3][0] = float(input("x4: "))
points[3][1] = float(input("y4: "))

def distance(p1, p2) -> float:
    return round(math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2), 3)

def area(p1, p2, p3) -> float:
    return round(abs((p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])), 3)

print("Площа паралелограма: ", area(points[0], points[1], points[2]))
print("Довжини діагоналей: ",
      distance(points[0], points[1]),
      distance(points[1], points[2]),
      distance(points[2], points[3]),
      distance(points[3], points[0])
)
