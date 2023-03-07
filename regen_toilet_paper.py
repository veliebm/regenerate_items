"""
Opens a webpage to order new toilet paper to your house.

Stops at the 2 factor auth step.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from cryptography import fernet
import pathlib

ENCODING = "utf-8"
KEY_PATH = "key"
ENCRYPTED_PASSWORD_PATH = "/tmp/encrypted_amazon_password"
USERNAME = "veliebm@gmail.com"
URL = "https://www.amazon.com/Amazon-Basics-2-Ply-Toilet-Paper/dp/B095CN96JS"
BUY_NOW_ID = "submit.buy-now"
USERNAME_CSS_SELECTOR = "input[type='email']"
PASSWORD_CSS_SELECTOR = "input[type='password']"
PLACE_ORDER_CSS_SELECTOR = "input[type='placeYourOrder1']"
TIMEOUT_TIME = 10
YOU_DO_THE_REST_MESSAGE = "That's as far as I go. If necessary, please complete 2 factor authentication and finish your purchase. Press enter to quit."
KEY_NOT_FOUND_ERROR_MESSAGE = "Please generate a key before running this script"
ENCRYPTED_PASSWORD_NOT_FOUND_ERROR_MESSAGE = (
    "Please refresh your credentials before running this script"
)


def main():
    password = get_password()
    driver = webdriver.Chrome()
    driver.get(URL)

    element = driver.find_element(By.ID, BUY_NOW_ID)
    element.click()

    element = WebDriverWait(driver, TIMEOUT_TIME).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, USERNAME_CSS_SELECTOR))
    )
    element.send_keys(USERNAME)
    element.send_keys(Keys.RETURN)
    element = WebDriverWait(driver, TIMEOUT_TIME).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, PASSWORD_CSS_SELECTOR))
    )
    element.send_keys(password)
    element.send_keys(Keys.RETURN)

    input(YOU_DO_THE_REST_MESSAGE)


def get_password() -> str:
    """Returns the decrypted password for the user using their stored encrypted password."""
    try:
        key = pathlib.Path(KEY_PATH).read_text()
    except FileNotFoundError:
        raise RuntimeError(KEY_NOT_FOUND_ERROR_MESSAGE)
    try:
        encrypted_password = pathlib.Path(ENCRYPTED_PASSWORD_PATH).read_text()
    except FileNotFoundError:
        raise RuntimeError(ENCRYPTED_PASSWORD_NOT_FOUND_ERROR_MESSAGE)

    reference_key = fernet.Fernet(key)
    return str(reference_key.decrypt(encrypted_password), encoding=ENCODING)


if __name__ == "__main__":
    main()
