s=input("Enter a sentence: ")

# Split into words, sort, and join back
words=s.split()
words.sort()

# Print sorted words
print("Sorted sentence:")
print(" ".join(words))
