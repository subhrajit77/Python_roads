class Mammal:
    def walk(self):
        print("I can walk")

class Dog(Mammal):
    def bark(self):
        print("I can bark")

class Cat(Mammal):
    pass

dog1 = Dog()
dog1.walk()
dog1.bark()

cat1 = Cat()
cat1.walk()