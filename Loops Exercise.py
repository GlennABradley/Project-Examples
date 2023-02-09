
#  ----------
#    PART 1
#  ----------
word = "supercalifragilisticexpialidocious"

# Write a for loop that prints out each character in the above "word" variable

# for char in word:
   #  print(char)


# Write a while loop that does the same thing!
idx = 0
while idx < len(word):
    print (word [idx])
    idx += 1


#  ----------
#    PART 2
#  ----------
# Write a while loop that prints the even numbers from 100 to 140 (including 140)

num = 100
while num is <= 140:
    print (num)
    num += 2


# Write a for loop that does the same thing (with range())

for num in range (100, 142, 2):
    print (num)

#  ----------
#    PART 3
#  ----------
# Write a loop that asks a user to input the passphrase "sillygoose" and keeps asking them to do so until they comply:

answer = input ("Could you please enter the passphrase? ")

while answer != "sillygoose":
    print ("Please enter the correct passphrase!")