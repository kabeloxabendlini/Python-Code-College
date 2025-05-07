def my_function(name, surname):
    print("Hello " + name + " " + surname)

my_function(name = "Kabelo,", surname = "Xabendlini")
my_function(name = "David,", surname = "Koen")
my_function(name = "Thozamile,", surname = "Xabendlini")
my_function(name = "Samkelo,", surname = "Limako")
my_function(name = "Werner,", surname = "van Niewenhuizen")

def my_pet(name, pet="dog"):
    print(f"This is my {pet} and his name is {name}")

my_pet("Spot", "cat")

def math(one, two, three=""):
         print(f"{one} is here. {two} is here. {three} is here ?")

math("gkhjgh", "ygtgf", "hafgsgfd")

junior_movies = {
      "name": "Scary Movie",
      "age-restriction": 17
}

def ticketing(name, age):
    print(f"Hello {name} you are welcomed to watch the following:\n(junior_movies(/)")

    if age > 16:
         print(f"Or you could watch this:\n(adult_movie{"name"})")

ticketing("David", 19)

def pizza(*toppings):
    print("You have ordered a pizza with the following: " + toppings)

def build_profile(first, last, **user_info):
     
    # ***Build a dictionary containing everything we know about a user,***
    user_info["first_name"] = first
    user_info["last name"] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                               field= 'physics')

print(user_profile)
     