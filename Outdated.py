# List of month names
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    try:
        user_entry = input("Enter date (e.g., September 8, 1636 or 9/8/1636): ")

        if "/" in user_entry:
            # Handling the format mm/dd/yyyy
            month, day, year = user_entry.split("/")
            month = int(month)
            day = int(day)
            year = int(year)

            if month not in range(1, 13):
                print("Invalid month. Please enter a month between 1 and 12.")
                continue
            if day not in range(1, 32):
                print("Invalid day. Please enter a day between 1 and 31.")
                continue

            print(f"{year:04d}-{month:02d}-{day:02d}")
            break

        else:
            # Handling the format Month day, year
            parts = user_entry.split()
            if len(parts) != 3:
                print("Invalid format. Please enter a valid date.")
                continue

            month_str, day, year = parts
            day = day.rstrip(",")  # Remove trailing comma if present

            for index, month_name in enumerate(months):
                if month_name.lower() == month_str.lower():
                    new_month = index + 1
                    break
            else:
                print("Invalid month name. Please enter a valid month.")
                continue

            day = int(day)
            year = int(year)

            if day not in range(1, 32):
                print("Invalid day. Please enter a day between 1 and 31.")
                continue

            print(f"{year:04d}-{new_month:02d}-{day:02d}")
            break

    except ValueError:
        print("Invalid input. Please enter a valid date (e.g., September 8, 1636 or 9/8/1636).")
    except Exception as e:
        print(f"An error occurred: {e}")
        break
