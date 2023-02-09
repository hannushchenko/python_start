file = open("classes.txt", 'w+')
class Dog:
    def __init__(self):
        name = input("name: ")
        if len(name) > 3:
            self.name = name
        else:
            self.name = None

        age = input("age: ")
        if int(age) >= 0:
            self.age = age
        else:
            self.age = 0

        color = input("color: ")
        if color in ("black", "yellow", "white", "orange"):
            self.color = color
        else:
            self.color = "black"

        male = input("male(f/m): ")
        if male in ("f", "F") :
            self.male = False
        else:
            self.male = True


dogList = []
# bobik = Dog("bobik", 3, "orange")
# toma = Dog("Toma", 11, "white", False)
# lila = Dog("Lila", male=False)
# dogList.append(bobik)
# dogList.append(toma)
# dogList.append(lila)

new = Dog()
print(new.__dict__)
dogList.append(new)



for dog in dogList:
    file.write(str(dog.__dict__)+"\n")
