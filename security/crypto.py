from cryptography.fernet import Fernet

key = b'twicfIT9TC4hj5ujYExIwR7XRKdrcM-SNfokX-GgITI='

fernet = Fernet(key)

def encrypt(value):
    return fernet.encrypt(value.encode()).decode()

def decrypt(value):
    return fernet.decrypt(value.encode()).decode()