from random import randint

num_dice = int(input("how many dice are you rolling? "))
num_sides = int(input ("how many sides on each die? "))

# Will Loop as long as the user wants until they quit "q"
# Using break, you exit the loop
# "for" loop will run the code as much as user inputs
# True runs forever as any user input is acceptable

while True:
    result = "|"
    for die in range (num_dice):
        rand = randint (1, num_sides)
        result += f"{rand}|"
    print(result)
    reply = input ("Roll again? (q to quit)")
    if reply == "q":
        break





