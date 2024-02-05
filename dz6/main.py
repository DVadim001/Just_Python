class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


User1 = Person(name='Pavel', age=25)
User2 = Person(name='Misha', age=30)

print(User1.name)
print(User1.age)
print(User2.name)
print(User2.age)
