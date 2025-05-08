from pathlib import Path
path = Path('Learning_python.txt')
path.write_text("I love programming.")

import Learning_python

# Read the entire file and print it
with open("Learning_python.txt") as file:
    contents = file.read()
    print("Printing entire file contents:\n")
    print(contents)

print("\n" + "-"*50 + "\n")

# Read the file line by line into a list and loop over it
with open("Learning_python.txt") as file:
    lines = file.readlines()

print("Printing file contents line by line:\n")
for line in lines:
    print(line.strip())