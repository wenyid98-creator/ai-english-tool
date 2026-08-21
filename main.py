print("English text Analyzer V0.3")

text = input("please enter your sentence:")

words = text.split()

print("Total words:",len(words))

print()

print("Long words:")
long_words=0
for word in words:
    if len(word) > 5:
        long_words = long_words + 1
        print("-",word)
print("Number of long words",long_words)
if long_words>=3:
    print("This is a vocabulary-rich sentence.")
else:
    print("This sentence is relatively simple.")
