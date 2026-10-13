#!pip install pycryptodome

from Crypto.Cipher import DES

def des_encrypt(key, text):
 cipher = DES.new(key, DES.MODE_ECB)
 return cipher.encrypt(text.encode()) #converts string into bytes

def des_decrypt(key, cipher_text):
 cipher = DES.new(key, DES.MODE_ECB)
 return cipher.decrypt(cipher_text).decode().strip() #converts bytes to string

key = b'mynewkey'
text = "Everyone"

cipher_text = des_encrypt(key, text)
print("Cipher", cipher_text)

plain_text = des_decrypt(key, cipher_text)
print("Plain Text:", plain_text)
