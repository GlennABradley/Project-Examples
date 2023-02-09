unit = input ("What unit are you using? ")
temp = int(input ("What temperature is the water? "))

# f - 212
# c - 100
# k - 373

if unit == "f":
    if temp == 212:
        print ("The water is boiling!!!!")
    else:
        print ("The water isn't boiling. Must hit 212F")
if unit == "c":
    if temp == 100:
        print ("The water is boiling!!!!")
    else:
        print ("The water isn't boiling. Must hit 100C")
if unit == "k":
    if temp == 373:
        print ("The water is boiling!!!!")
    else:
        print ("The water isn't boiling. Must hit 373K")