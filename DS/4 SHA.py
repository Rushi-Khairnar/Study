import hashlib
text = input("Enter the value to encode: ")

result = hashlib.sha1(text.encode())

print("The hexadecimal equivalent if SHA is: ", result.hexdigest())
