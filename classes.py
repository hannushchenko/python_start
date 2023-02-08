class Dog:
    def __init__(self, name=None, age=0, color='black', male=True):
        self.name = name
        self.age = age
        self.color = color
        self.male = male


bobik = Dog("bobik", 3, "orange")
toma = Dog("Toma", 11, "white", False)
lila = Dog("Lila", male=False)

