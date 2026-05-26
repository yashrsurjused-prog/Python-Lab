import string

# Input from user
text = input()

# Empty string to store result
result = ""

# Loop through each character
for ch in text:
    if ch not in string.punctuation:
        result += ch

# Print the result
print(result)
