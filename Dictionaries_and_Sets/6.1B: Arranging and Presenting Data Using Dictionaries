def word_counter(word):
    # Initialize an empty dictionary to store the frequency of each character
    frequency = {}

    # Iterate through each character in the word
    for char in word:
        if char != ' ':  # Skip spaces
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1

    return frequency

# Call the word_counter function with the string "Mississippi" and print the result
print(word_counter("Mississippi"))