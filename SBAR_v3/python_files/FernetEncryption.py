from cryptography.fernet import Fernet

# Key and Fernet object for handling encryption and decryption.
key = b'kEPncDyAkuPliWytKOTlvE0ujiAR44lRTmjGEouyT5U='
f = Fernet(key)

def encrypt(data):
    return f.encrypt(data.encode()).decode()

def decrypt(data):
    return f.decrypt(data.encode()).decode()