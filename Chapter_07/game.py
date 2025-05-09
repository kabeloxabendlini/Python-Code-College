age = input("What is you age ?")

if int(age) > 18:
    print("Have a beer!")
elif int(age) < 18:
    print("Not Today.")

    prompt = "\nTell me something, and I will repeat it back to you:"
    prompt += "\nEnter 'quit' to end the program, "
    message = ""

while message != 'quit':
    message = input(prompt)
    print(message)

#//########################################################################################################//

# lives = 5
# mission = True 
# game = ""

# game_is_active = True 

# while game_is_active:
    
#     if lives == 0:
#         game_is_active: False
#     elif mission == False:
#         game_is_active = False
#     elif game == "quit":
#         game_is_active = False