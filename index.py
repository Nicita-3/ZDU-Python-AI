from pprint import pprint
groups = set()
class StudentZDU:
    def __init__(self, name, age, curs, group) -> None:
        self.name = name
        self.age = age
        self.curs = curs
        self.group = group
        print(f"Student {self.name} init!")
    
    def __repr__(self):
        return f"StudentZDU(name={self.name}, age={self.age}, curs={self.curs}, group={self.group})"
 
    def __add__(self, other) -> list:
        return [self, other]

p1 = StudentZDU("Nicita3", 18, 2, "23Бд-СОінф")
groups[p1.group] = p1

p2 = StudentZDU("Dima", 19, 2, "23Бд-СОінф")
groups[p2.group] = p2

pprint(p1 + p2)
pprint(groups)