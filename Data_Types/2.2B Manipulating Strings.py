a = input("Sentence: ")
b = input("Word to look for in sentence: ")

# Convert th sentence to lowercase for case-sensitive counting
c = a.lower()

# Count occurrences of the word in the sentence
d = c.count(b.lower())

print(f'There are {d} occurrences \'{b}\' in the sentence.')