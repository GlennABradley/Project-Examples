## Sentiment Analysis Project ##

from textblob import TextBlob
import pyttsx3
import art

header = art.text2art("House De Huncho")
print(header)
engine = pyttsx3.init()
name = input ("What is your name? ")
engine.say(f"How are you feeling today {name}? Could you please enter your employee statement when requested! ")
engine.runAndWait()


print("Enter your employee wellness statment please! ")
phrase = input ("> ")
testimonial = TextBlob(phrase)
while testimonial.sentiment.polarity < 0.5:
    engine.say(f"{name} I think you can be a bit more positive than that! Lets try again! ")
    engine.runAndWait()
    print('t(-_-t) ')
    print ("More positivity! You're depressing! ")
    phrase = input("> ")
    testimonial = TextBlob(phrase)

print('(っ◕‿◕)っ ')
print ("We're happy to see you happy!! ")
engine.say(f"Keep being the best you possible {name}! ")
engine.runAndWait()
