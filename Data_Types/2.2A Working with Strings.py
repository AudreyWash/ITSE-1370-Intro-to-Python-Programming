first_string = input("Word to convert: ")

count = int(input("How many letters at the end of the word should be converted? "))

# Validate the count
if count > len(first_string):
    print("Count is greater thn the length of the word. Converting the entire word to uppercase.")
    count = len(first_string)

# Get the part of the string to keep as it is
start_of_string = first_string[:-count]

#Get the part of the string to convert to uppercase
end_of_string = first_string[-count:].upper()

# Concatenate the unchanged part and the transformed part
result = start_of_string + end_of_string

printr(result)