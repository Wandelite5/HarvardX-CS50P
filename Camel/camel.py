camelCase = input("camelCase: ")
snake_case = ""

for char in camelCase:
    if char.isupper():
        snake_case += "_" + char.lower()
    else:
        snake_case += char
snake_case = snake_case.lstrip("_")
print(snake_case)
