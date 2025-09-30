# Напишіть покрокову гру, яка дозволяє посадити на планету
# космічний корабель. Гра представляє собою серію кроків, для яких треба
# вводити координати наступної точки, до якої має переміститися
# корабель.
# Позиціонування корабля, планети та перешкод задається
# псевдографічним символьним інтерфейсом і виводиться на екран з
# кожним кроком.
# Гравець виграє, якщо космічний корабель заходить в атмосферу
# планети (окіл на 1 більший за розмір планету).
# Космічний корабель розбивається об перешкоду, якщо попадає у
# одиничний її окіл або на саму перешкоду або ж його лінійний шлях
# перетинає цю перешкоду чи її окіл.
# Космічний корабель займає одне ігрове поле 1*1, перешкоди (до чотирьох на гру)
# мають варіативні розміри квадратів від 1*1 до 3*3,
# розміри планети варіюються від 4*4 до 5*5.
# Між перешкодами має бути відстань мінімум 3 клітинки.
# Розміщення всіх ігрових елементів задається випадковим чином на початку гри.
# Реалізація має бути на основі ООП.
import sys, io
import os
import random
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
renderX = 70 # min 30+-
renderY = 30 # min 20+-


class Rocket:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.d = 1
        self.textures = [["🚀"]]

    
class Planet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.d = random.randint(4, 5)
        self.textures = [["🟩" for i in range(self.d)] for i in range(self.d)]

class Obstacle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.d = random.randint(1, 3)
        self.textures = [["🟨" for i in range(self.d)] for i in range(self.d)]

class Render:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.objs = []

    def __str__(self):
        screen = [["  " for _ in range(self.w)] for _ in range(self.h)]
        for obj in self.objs:
            for i in range(obj.d):
                for j in range(obj.d):
                    symbol = obj.textures[i][j]
                    if symbol.strip():
                        y = obj.y + i
                        x = obj.x + j
                        if 0 <= x < self.w and 0 <= y < self.h:
                            screen[y][x] = symbol

        top_numbers = "   " + "".join(f"{i%10:2}" for i in range(self.w))
        lines = [top_numbers]

        for idx, row in enumerate(screen):
            lines.append(f"{idx:2} " + "".join(row))

        return "\n".join(lines)
    
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

# Інпут корд
def getCordsToStr(string):
    try:
        strCords = input(string)
        numbers = [int(x) for x in strCords.split()]
        return {
            "x": numbers[0],
            "y": numbers[1]
        }
    except ValueError:
        print("ПОМИЛКА ВВОДУ! Спробуйте ще раз...")
        return getCordsToStr(string)

# Інпут числа
def getInt(string, min, max):
    try:
        k = int(input("Введіть кількість перешкод від 1 до 4: "))
        if k < min or k > max:
            print("ПОМИЛКА ВВОДУ! Спробуйте ще раз...")
            return getInt(string, min, max)
        else:
            return k
    except ValueError:
        print("ПОМИЛКА ВВОДУ! Спробуйте ще раз...")
        return getInt(string, min, max)

def generateObstacleCoords(num, w, h, min_distance=3, max_size=3):
    coords = []

    i = 0
    max_i = 1000
    while len(coords) < num and i < max_i:
        size = random.randint(1, max_size)
        x = random.randint(0, w - size - 1)
        y = random.randint(0, h - size - 1)

        ok = True
        for ox, oy, od in coords:
            if abs(x - ox) < od + size + min_distance and abs(y - oy) < od + size + min_distance:
                ok = False
                break

        if ok:
            coords.append((x, y, size))

        i += 1

    return coords


# Менеджер інпуту №2
def startDefaultGame():
    data = {
        "rocket": None,
        "planet": None,
        "obstacles": []
    }
    data["rocket"] = Rocket(renderX // 2, 0)
    data["planet"] = Planet(renderX // 2, renderY - 3)

    obstacle_coords = generateObstacleCoords(4, renderX, renderY)

    for x, y, size in obstacle_coords:
        obs = Obstacle(x, y)
        obs.d = size
        obs.textures = [["🟨" for _ in range(size)] for _ in range(size)]
        data["obstacles"].append(obs)

    return data

# Менеджер інпуту
def startGame():
    data = {
        "rocket": None,
        "planet": None,
        "obstacles": []
    }
    rocketCords = getCordsToStr("Введіть координати корабля x y: ")
    data["rocket"] = Rocket(rocketCords["x"], rocketCords["y"])
    planetCords = getCordsToStr("Введіть координати планети x y: ")
    data["planet"] = Planet(planetCords["x"], planetCords["y"])
    k = getInt("Введіть кількість перешкод від 1 до 4: ", 1, 4)
    i = 1
    while (i <= k):
        obstacleCords = getCordsToStr(f"Введіть координати перешкоди №{i} x y: ")
        data["obstacles"].append(Obstacle(obstacleCords["x"], obstacleCords["y"]))
        i += 1
    return data

# game = startGame()
game = startDefaultGame()

def isСollision(x, y, obstacles):
    for obs in obstacles:
        if (obs.x - 1 <= x <= obs.x + obs.d) and (obs.y - 1 <= y <= obs.y + obs.d):
            return True
    return False

def isPathBlocked(x1, y1, x2, y2, obstacles):
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    if steps == 0:
        return isСollision(x1, y1, obstacles)
    for i in range(steps + 1):
        xi = x1 + round(i * dx / steps)
        yi = y1 + round(i * dy / steps)
        if isСollision(xi, yi, obstacles):
            return True
    return False

def isPlanetReached(x, y, planet):
    if (planet.x - 1 <= x <= planet.x + planet.d) and (planet.y - 1 <= y <= planet.y + planet.d):
        return True
    return False

r = Render(renderX, renderY)
r.objs.append(game["planet"])
r.objs.extend(game["obstacles"])
r.objs.append(game["rocket"])

prev_x = game["rocket"].x
prev_y = game["rocket"].y

Render.clear()
print(r)

while True:
    rocketCords = getCordsToStr(f"Введіть координати корабля x({prev_x}) y({prev_y}) (мінус для виходу): ")

    x = rocketCords["x"]
    y = rocketCords["y"]
    if x < 0 or y < 0:
        print("Вихід з гри...")
        break

    if isPathBlocked(prev_x, prev_y, x, y, game["obstacles"]):
        print("Корабель розбився об перешкоду! 💥💥💥💥💥💥")
        break

    
    game["rocket"].x = x
    game["rocket"].y = y

    if isPlanetReached(x, y, game["planet"]):
        Render.clear()
        print(r)
        print("Успішна посадка на планету!")
        break

    Render.clear()
    print(r)

    prev_x = x
    prev_y = y