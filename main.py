print("=== AI English Learning Tool V0.2 ===")

text = input("Enter an English sentence: ")

words = text.split()

print()
print("Your words are:")

for word in words:
    print("-", word)

print()
print("Total words:", len(words))