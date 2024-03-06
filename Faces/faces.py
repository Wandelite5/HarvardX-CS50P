def convert(text):
    return(text).replace(":)", "🙂").replace(":(", "🙁")

def main():
   user = input("what do want to say ?")
   converted_text = convert(user)
   print(converted_text)

main()

