from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class AuthPage:
    def __init__(self, driver: WebDriver) -> None:
        self.__url = "https://id.atlassian.com/login?application=trello&continue=https%3A%2F%2Ftrello.com%2Fauth%2Fatlassian%2Fcallback%3Fdisplay%3DeyJ2ZXJpZmljYXRpb25TdHJhdGVneSI6InNvZnQifQ%253D%253D&display=eyJ2ZXJpZmljYXRpb25TdHJhdGVneSI6InNvZnQifQ%3D%3D&prompt=login"
        self.__driver = driver

    def go(self):
        self.__driver.get(self.__url)
    
    def login_as(self, email: str, password: str):
        self.__driver.find_element(By.CSS_SELECTOR, 'input[name="username"]').send_keys(email)
        self.__driver.find_element(By.CSS_SELECTOR, "#login-submit").click()
        self.__driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        self.__driver.find_element(By.CSS_SELECTOR, "#login-submit").click()

    def get_current_url(self):
        return self.__driver.current_url