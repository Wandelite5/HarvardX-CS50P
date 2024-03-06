'''
In a file called playback.py, implement a program in Python that prompts the user for input and
then outputs that same input, replacing each space with ... (i.e., three periods).
'''
user = input("what are you saying? ").replace(" ", "...")
print(user)

#using split and join methods
#text = input("what are you saying? ").split()
#replaced_text = "...".join(text)
#print(replaced_text)

