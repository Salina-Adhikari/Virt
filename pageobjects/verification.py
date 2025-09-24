from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Verification:
    verification_xpath="input[class='disabled:cursor-not-allowed']"
    verify_button_xpath="//button[normalize-space()='Verify Code']"

    def __init__(self, driver):
        self.driver = driver
    def set_verification(self,validcode):
        verification_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.verification_xpath)))
        verification_field.clear()
        verification_field.send_keys(validcode)
    def click_verification_button(self):
        self.driver.find_element(By.XPATH,self.verify_button_xpath).click()