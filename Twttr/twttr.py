user = input("Input: ")
consonant = ""

for char in user:
    if char not in "aeiouAEIOU":
        consonant += char
print(f'Output: {consonant}')


