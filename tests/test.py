from typing import OrderedDict
from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open("key.key", "wb") as filekey:
    filekey.write(key)

fernet = Fernet(key)


with open("test.txt", "rb") as file:
    original = file.read()

encrypted = fernet.encrypt(original)

with open('test.txt', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)