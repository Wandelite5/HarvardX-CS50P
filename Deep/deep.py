
#match
user = input("what's the answer to the Great Question of Life, the Universe and Everything? ").casefold().strip()
match user:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")

#using if & elif
'''user = input("what's the answer to the Great Question of Life, the Universe and Everything? ").casefold().strip
if user == "42" or "forty-two" or "forty two":
    print("Yes")
else:
    print("No")'''
