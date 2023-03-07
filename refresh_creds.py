"""
Refreshes your Amazon credentials by asking you for your password.
"""

from cryptography import fernet
import pathlib
import getpass

KEY_PATH = "key"
ENCRYPTED_PASSWORD_PATH = "/tmp/encrypted_amazon_password"
PASSWORD_PROMPT = "Please enter your Amazon password. This will be deleted from the system upon reboot: "
ENCODING = "utf-8"

try:
    key = pathlib.Path(KEY_PATH).read_text()
except OSError:
    raise RuntimeError("Please generate a key before running this script")

reference_key = fernet.Fernet(key)

encrypted_password = reference_key.encrypt(
    bytes(
        getpass.getpass(PASSWORD_PROMPT),
        ENCODING,
    )
)

pathlib.Path(ENCRYPTED_PASSWORD_PATH).write_text(str(encrypted_password, ENCODING))
