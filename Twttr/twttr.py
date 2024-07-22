user_entry = input("Input: ")
consonant = ""

for char in user_entry:
    if char not in "aeiouAEIOU":
        consonant += char
print(f'Output: {consonant}')


