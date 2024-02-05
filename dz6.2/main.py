class Animal:
    def __init__(self, new_sound):
        self.new_sound = new_sound

    def make_sound(self, new_sound):
        print(new_sound)


class Dog(Animal):
    def __init__(self, new_sound):
        super().__init__(new_sound)


class Cat(Animal):
    def __init__(self, new_sound):
        super().__init__(new_sound)


class Cow(Animal):
    def __init__(self, new_sound):
        super().__init__(new_sound)


dog1 = Dog('Гав')
cat1 = Cat('Мяу')
cow1 = Cow('Му')

dog1.make_sound('Гав')
cat1.make_sound('Мяу')
cow1.make_sound('Му')
