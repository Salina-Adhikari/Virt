from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Certificate:
    registration_number_xpath ="//input[@placeholder='Enter your registration number']"
    per_country_dropdown_xpath="//button/div/span[normalize-space()='Select your Preferred Countries']"
    per_country_search_xpath="//input[@placeholder='Search...']"
    per_institution_xpath="//button[@aria-describedby='«r3t»-form-item-description']"
    company_file_xpath="//input[@type='file']"
    educational_file_xpath="//input[@type='file']"
    submit_button_xpath="//button[normalize-space()='Submit']"

    def __init__(self, driver):
        self.driver = driver
    def set_registration_number_xpath(self,number):
        registration_field=WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,self.registration_number_xpath))
        )
        registration_field.clear()
        registration_field.send_keys(number)
    def click_country_dropdown(self):
        country_field=WebDriverWait(self.driver, 10).until((EC.element_to_be_clickable((By.XPATH,self.per_country_dropdown_xpath))))
        country_field.click()

    def set_per_country_search(self,country):
        country_search_field=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.per_country_search_xpath))
        )
        country_search_field.send_keys(country)
    def set_per_institution_xpath(self,institution):
        per_institution_field=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.per_institution_xpath))
        )
        per_institution_field.clear()
        per_institution_field.send_keys(institution)
    def set_company_file_xpath(self,filepath_1):
        company_file_field=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,self.company_file_xpath)))
        company_file_field.send_keys(filepath_1)
    def set_educational_file_xpath(self,filepath_2):
        educational_file_field=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,self.educational_file_xpath)))
        educational_file_field.send_keys(filepath_2)
    def click_submit_button(self):
        submit_button=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,self.submit_button_xpath)))
        submit_button.click()

