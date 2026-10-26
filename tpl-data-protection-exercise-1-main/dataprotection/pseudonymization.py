from cryptography.fernet import Fernet

"""
TODO:
- Generate a key once and reuse it for both pseudonymization and restoration. In a real system, this key would be securely stored.
"""
key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b"my deep dark secret")


def pseudonymize_names(names):
    """
    TODO: Encrypt each name with Fernet symmetric encryption.
    - return list of encrypted names
    """

    return [f.encrypt(name.encode('utf-8')) for name in names]


def restore_names(encrypted):
    """
    TODO: Decrypt previously pseudonymized names.
    - return list of decrypted names
    """
    

    return [f.decrypt(name).decode('utf-8') for name in encrypted]