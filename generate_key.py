"""
Encrypts a password for you. Also writes a key to unencrypt it.
"""

from cryptography import fernet
import pathlib
import getpass

key = fernet.Fernet.generate_key()
reference_key = fernet.Fernet(key)

encrypted_password = reference_key.encrypt(
    bytes(getpass.getpass("Please enter a password to encrypt: "), "utf-8")
)

pathlib.Path("/tmp/encrypted_amazon_password").write_text(str(encrypted_password))
pathlib.Path("/tmp/key").write_text(str(key))
