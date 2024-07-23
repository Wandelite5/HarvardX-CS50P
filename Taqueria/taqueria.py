menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total_amt = 0
while True:
    try:
        user_entry = input("Item: ").title()
        if user_entry == "Exit":
            print("Exiting Program")
            break
        if user_entry.title() in menu:
            total_amt += menu[user_entry] 
            print(f"${total_amt}")
    except EOFError: 
        print()
        break 