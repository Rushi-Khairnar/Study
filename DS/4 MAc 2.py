import hmac, hashlib

key = b"secret-key"
msg = b"Transfer $100 to Alice"
mac1 = hmac.new(key, msg, hashlib.sha256).hexdigest()
print("Original MAC (mac1) :", mac1)

tampered_msg = b"Transfer $9999 to Bob"

mac2 = hmac.new(key, tampered_msg, hashlib.sha256).hexdigest()
print("Tampered MAC (mac2) :", mac2)

is_valid = hmac.compare_digest(mac1, mac2)

is_tampered = not is_valid
print("Is data tampered?:", is_tampered)
