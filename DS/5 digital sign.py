import rsa

public_key, private_key = rsa.newkeys(512)

message = "Data Security Practical"

signature = rsa.sign(message.encode(), private_key, 'SHA-256')
print("Digital Signature Created.")

try:
    rsa.verify(message.encode(), signature, public_key)
    print("Signature Verified Successfully.")
except:
    print("Signature Verification Failed.")
