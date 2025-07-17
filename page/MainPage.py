from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver

    def get_current_url(self) ->str:
        return self.__driver.current_url
    
    def open_menu(self):
        self.__driver.find_element(By.CSS_SELECTOR, 'button[data-testid=header-member-menu-button]').click()
        
    def get_account_info(self):
        menu = self.__driver.find_element(By.CSS_SELECTOR, 'button[data-testid=header-member-menu-button]')
        div = menu.find_element(By.CSS_SELECTOR, 'div')
        divs = div.find_element(By.CSS_SELECTOR, 'div')[1]
        name = divs[0].text
        email = divs[1].text

        return [name, email]