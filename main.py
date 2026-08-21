print("---ILL BE SOMEBODY IN FUTURE---")
text = input("please enter your sentence: ")
words = text.split()

for word in words:
    print("" + word)
    print("-")

print("Your total words are: ", len(words))