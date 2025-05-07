class Myself:

    def __init__(self, name):
        self.name = name
        self.species = "Human"

    def greet(self):
        print(f"Hello, I'm {self.name}")

class MyDog(Myself):

    def __init__(self, my_dog_name):
        super().__init__(my_dog_name)
    
    def greet(self):
        print(f"Boom {self.name}")

Pammy = MyDog("Pam")
Sofie = MyDog("Sofie")

print(Pammy.name)
Sofie.greet()