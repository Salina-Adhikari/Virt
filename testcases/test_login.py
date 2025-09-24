import time
from selenium.webdriver.common.by import By
import pytest
from utilities import  customLogger
from utilities import readProperties
from pageobjects.LoginPage import SignupPage
from utilities.readProperties import ReadConfig


class Test_1_Sigin:
    url=ReadConfig.getApplicationURL()
    email=ReadConfig.getemail()
    firstname=ReadConfig.getfirstname()
    lastname=ReadConfig.getlastname()
    phonenumber=ReadConfig.getphonenumber()
    password=ReadConfig.getpassword()
    confirm_password=ReadConfig.getemail()


    def test_login(self,setup):
        self.driver=setup
        time.sleep(2)
        self.driver.get(self.url)
        self.sp=SignupPage(self.driver)
        self.sp.click_signup()
        time.sleep(2)
        self.driver.maximize_window()
        self.sp.click_agree()
        self.sp.click_continue()
        time.sleep(2)
        self.sp.set_firstname(self.firstname)
        self.sp.set_lastname(self.lastname)
        self.sp.set_email(self.email)
        self.sp.set_phonenumber(self.phonenumber)
        self.sp.set_password(self.password)
        self.sp.set_confirm_password(self.password)
        time.sleep(2)
        self.sp.click_next_button()
        time.sleep(2)


