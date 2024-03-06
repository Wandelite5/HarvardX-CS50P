#learnt the method startswith
client = input("Greeting: ").casefold().strip()

if client.startswith("hello" or "hello, Newman" or "hello there"):
    print("$0")
elif client.startswith("h"):
     print("$20")
else:
     print("$100")
