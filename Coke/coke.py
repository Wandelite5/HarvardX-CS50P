total_amt = 50
amt_paid = 0

print(f'Amount Due: {total_amt}')

while amt_paid < total_amt:
    user = int(input("Insert Coin: "))
    if user in (25, 10, 5):
        amt_paid += user
        result = total_amt - amt_paid
        if amt_paid < total_amt:
            print(f'Amount Due: {result}')
        if amt_paid >= total_amt:
            print(f'Change Owed: {amt_paid - total_amt}')
    else:
        print(f'Amount Due: {total_amt - amt_paid}')
