with open("classes.txt", 'r') as filer:
    read = filer.read()
    print(read)


class Dog:
    def __init__(self):
        name = input("name: ")
        if len(name) > 2:
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
new = Dog()
dogList.append(new)
# bobik = Dog("bobik", 3, "orange")
# toma = Dog("Toma", 11, "white", False)
# lila = Dog("Lila", male=False)
# dogList.append(bobik)
# dogList.append(toma)
# dogList.append(lila)

with open("classes.txt", 'a+') as filea:
    for dog in dogList:
        filea.write(str(dog.__dict__)+"\n")
        print(dog.__dict__)
