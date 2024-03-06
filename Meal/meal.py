def main():
    user = input("what time is it? ")
    converted_time = convert(user)
    if 7 <= converted_time <= 8:
        print(f'breakfast time')
    elif 12 <= converted_time <= 13:
        print(f'lunch time')
    elif 18 <= converted_time <= 19:
        print(f'dinner time')

def convert(time):
    hours, minutes = time.split(":")
    return int(hours) + int(minutes)/60


if __name__ == "__main__":
    main()
