class person:
    name = "Joe"
    age = 31
    gender = "Male"

    def eat(self):
        print("Eating")

p = person()
print(p.gender)
print(p.name)

p.eat()