from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

priv = rsa.generate_private_key(65537, 2048)
pub = priv.public_key()
pad = padding.OAEP(padding.MGF1(hashes.SHA256()),
hashes.SHA256(), None)

msg = b"secret data"
cipher = pub.encrypt(msg, pad)
print("Ciphertext:", cipher[:20], "...")

decrypted = priv.decrypt(cipher, pad)
print("Decrypted :", decrypted)
print("Decrypted :", decrypted.decode('utf-8'))
