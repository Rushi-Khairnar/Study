import hmac, hashlib

key = b"secret-key"
msg_sent = b"Transfer $100 to Alice"
mac1 = hmac.new(key, msg_sent, hashlib.sha256).hexdigest()
print("Original MAC (mac1) :", mac1)


msg_received = b"Transfer $100 to Alice"


mac2 = hmac.new(key, msg_received, hashlib.sha256).hexdigest()
print("Received MAC (mac2) :", mac2)


is_valid = hmac.compare_digest(mac1, mac2)
print("Is the message valid? :", is_valid)
import hmac, hashlib

