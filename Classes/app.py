class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()    
point1.move()
point2= Point()
point2.x=5
print(point2.x)

class Person:
    def __init__(self, name):
        self.name=name

    def talk(self):
        print(f"Hi, I am {self.name}")

person1 = Person("Ashish")
# print(person1.name)
person1.talk()           