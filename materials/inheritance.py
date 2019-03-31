class Animal:
    def __init__(self, name, age, alive=True, hungry=False):
        self.name = name
        self.age = age
        self.alive = alive
        self.hungry = hungry

    def description(self):
        return "Name of an animal is {} and it is {} years old".format(self.name, self.age)

    def is_alive(self):
        return self.alive

    def is_hungry(self):
        return self.hungry


class Parrot(Animal):
    def say(self):
        return 'Krrr...'

    def type(self):
        return 'Domestic'


class Panther(Animal):
    def say(self):
        return 'Shhh...'

    def type(self):
        return 'Wild'


parrot = Parrot('Jake', 2)
print(parrot.description())
print(parrot.is_alive())
print(parrot.is_hungry())
print(parrot.say())
print(parrot.type())

panther = Panther('Sky', 3)
print(panther.description())
print(panther.is_alive())
print(panther.is_hungry())
print(panther.say())
print(panther.type())
