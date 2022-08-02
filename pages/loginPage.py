from selenium.webdriver.common.by import By


class LoginPage:
    USERNAME_FIELD = (By.NAME, "Username")
    PASSWORD_FIELD = (By.NAME, "Password")
    SIGN_BUTTON = (By.ID, "signin")

    def __init__(self, driver):
        self.driver = driver

    def enterUsername(self, username):
        self.driver.find_element(*LoginPage.USERNAME_FIELD).send_keys(username)

    def enterPassword(self, password):
        self.driver.find_element(*LoginPage.PASSWORD_FIELD).send_keys(password)

    def clickLoginButton(self):
        self.driver.find_element(*LoginPage.SIGN_BUTTON).click()
