# main.py
name = "Kabelo"
age = 19

# main.py
import main

def greet_user(name, age):
    print(f"Hello, {name}! You are {age} years old.") 
    
    # Use arguments from the external module
    greet_user(main.__name__, main.age)
    

