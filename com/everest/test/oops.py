class Employee:
    id = 0
    name = ""

    def __init__(self, name, id):
        self.id = id
        self.name = name

    def display(self):
        print("Id: %d\nName: %s" % (self.id, self.name))


emp1 = Employee("name1", 100)
emp2 = Employee("name2", 101)

emp1.display()
emp2.display()


class Animal:

    def speak(self):
        print("Animal Speaking")
    # child class Dog inherits the base class Animal


class Dog(Animal):
    def bark(self):
        print("dog barking")


d = Dog()
d.bark()
d.speak()

print(issubclass(Dog, Animal))
print(isinstance(d, Dog))
