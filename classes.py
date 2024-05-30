class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
point1.draw()


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("talk")


john = Person("John Smith")
print(john.name)
john.talk()
