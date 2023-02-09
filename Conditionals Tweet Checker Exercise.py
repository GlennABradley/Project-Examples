max_chars = 140
print ("*********************")
tweet = input("Enter Tweet Here: ")
chars_count = len(tweet)


if chars_count < max_chars:
    print(f" That {chars_count} character tweet will work, sent!")
else:
    print(f"That {chars_count} character tweet will not work it's {chars_count - max_chars} characters too long, not sent!")