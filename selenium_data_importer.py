from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from abstract_data_importer import AbstractDataImporter

url = 'https://sanalouhos.datadesk.hs.fi/'


class SeleniumDataImporter(AbstractDataImporter):
    def import_data(self) -> str:
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(service=Service(
            ChromeDriverManager().install()), options=options)

        driver.get(url)
        driver.find_element(By.CLASS_NAME, "button").click()
        html = driver.find_element(
            By.CLASS_NAME, "game-area-container").get_attribute('innerHTML')
        driver.close()
        return html
