from selenium import webdriver
from pages.loginPage import LoginPage
import pytest


class TestCaseLogin:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.loginPage = LoginPage(self.driver)
        self.driver.get("https://my.asos.com/identity/login")

    def login(self, username, password):
        self.loginPage.enterUsername(username)
        self.loginPage.enterPassword(password)
        self.loginPage.clickLoginButton()

    def test_log_in_registered_user(self):
        self.login("test1234@gmail.com", "test1234")

    def test_log_in_with_unregistered_user(self):
        self.login("testmail12@gmail.com", "test12345")

    def test_log_in_with_empty_email(self):
        self.login("", "test1234")

    def test_log_in_with_empty_password(self):
        self.login("testmail@gmail.com", "")

    def test_log_in_with_empty_email_and_password(self):
        self.login("", "")

    def teardown_method(self):
        self.driver.quit()


if __name__ == "__main__":
    pytest.main()
