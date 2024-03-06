user = input("File type: ").casefold().strip()
media_type = user.rsplit(".", 1)[-1]
if user.endswith(".gif"):
    print(f'image/{media_type}')
elif user.endswith((".jpg", ".jpeg")):
    print("image/jpeg")
elif user.endswith(".png"):
    print(f'image/{media_type}')
elif user.endswith(".pdf"):
    print(f'application/{media_type}')
elif user.endswith(".txt"):
    print("text/plain")
elif user.endswith(".zip"):
    print(f'application/{media_type}')
else:
    print("application/octet-stream")
