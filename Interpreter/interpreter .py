user = input("Expression: ").strip()

# Split the input into three parts based on spaces
x, operator, z = user.split()

# Check the operator and perform the corresponding operation
if operator == '+':
    w = int(x) + int(z)
    print(f'{w:.1f}')
elif operator == '-':
    w = int(x) - int(z)
    print(f'{w:.1f}')
elif operator == "*":
    user = int(x) * int(z)
    print(f"{user:.1f}")
elif operator == "/":
    user = int(x) / int(z)
    print(f"{user:.1f}")
else:
    print(f"{user} invalid input")
