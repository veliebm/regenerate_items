"""
Generates a key to encrypt and decrypt your password.
"""
from cryptography import fernet
import pathlib

KEY_PATH = "key"
ENCODING = "utf-8"

key = fernet.Fernet.generate_key()
pathlib.Path(KEY_PATH).write_text(str(key, ENCODING))
