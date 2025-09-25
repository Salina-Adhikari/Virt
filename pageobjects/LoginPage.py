from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.mail_helper import MailHelper

class SignupPage:
    signup_xpath = "//a[normalize-space()='Sign Up']"
    agree_xpath = "//button[@id='remember']"
    continue_xpath = "//button[normalize-space()='Continue']"
    firstname_css = "#«r0»-form-item"
    lastname_css = "#«r1»-form-item"
    email_css = "#«r2»-form-item"
    phonenumber_css = "#«r4»-form-item"
    password_xpath = "//input[@name='password']"
    confirm_password_xpath = "//input[contains(@name,'confirmPassword')]"
    next_button_xpath = "//button[normalize-space()='Next']"

    def __init__(self, driver):
        self.driver = driver

    def click_signup(self):
        self.driver.find_element(By.XPATH, self.signup_xpath).click()

    def click_agree(self):
        self.driver.find_element(By.XPATH, self.agree_xpath).click()

    def click_continue(self):
        self.driver.find_element(By.XPATH, self.continue_xpath).click()

    def set_firstname(self, firstname):
        firstname_field=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.firstname_css)))
        firstname_field.clear()
        firstname_field.send_keys(firstname)

    def set_lastname(self, lastname):
        lastname_field=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.lastname_css)))
        lastname_field.clear()
        lastname_field.send_keys(lastname)

    def set_email(self, email):
        email_field=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.email_css)))
        email_field.clear()
        email_field.send_keys(email)


    def set_password(self, password):
        self.driver.find_element(By.XPATH, self.password_xpath).clear()
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)

    def set_phonenumber(self,phonenumber):
        phonenumber_field=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.phonenumber_css)))
        phonenumber_field.clear()
        phonenumber_field.send_keys(phonenumber)


    def set_confirm_password(self,password):
        self.driver.find_element(By.XPATH, self.confirm_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.confirm_password_xpath).send_keys(password)

    def click_next_button(self):
        self.driver.find_element(By.XPATH, self.next_button_xpath).click()







