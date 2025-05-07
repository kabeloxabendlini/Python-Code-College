class Myself:

    def __init__(self, name):
        self.name = name
        self.species = "Human"

    def greet(self):  
        print(f"Hello, I'm {self.name}")

me = Myself("Kabelo")
not_me = Myself("Pam")

not_me.species = "Awesome"

print(not_me.species)
print(me.species)
