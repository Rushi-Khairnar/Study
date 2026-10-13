import hashlib
message = "Hello, world!"
hashed_message = hashlib.md5(message.encode())
print(hashed_message.hexdigest())
