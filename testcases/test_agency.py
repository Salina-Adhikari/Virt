import time
from selenium.webdriver.common.by import By
import pytest

from pageobjects.AgencyPage import AgencyPage
from pageobjects.verification import Verification
from utilities import  customLogger
from utilities import readProperties
from pageobjects.LoginPage import SignupPage
from utilities.readProperties import ReadConfig
from utilities.mail_helper import MailHelper

class Test_2_Sigin:
    url = ReadConfig.getApplicationURL()
    firstname = ReadConfig.getfirstname()
    lastname = ReadConfig.getlastname()
    phonenumber = ReadConfig.getphonenumber()
    password = ReadConfig.getpassword()
    name=ReadConfig.getname()
    role=ReadConfig.getrole()
    agency_email=ReadConfig.getagency_email()
    website=ReadConfig.getwebsite()
    address=ReadConfig.getaddress()
    country=ReadConfig.getcountry()



    def test_login(self, setup):
            self.driver = setup
            time.sleep(2)
            self.driver.get(self.url)
            self.sp = SignupPage(self.driver)
            self.verify=Verification(self.driver)
            self.agency=AgencyPage(self.driver)
            self.sp.click_signup()
            time.sleep(2)
            self.driver.maximize_window()
            self.sp.click_agree()
            self.sp.click_continue()
            time.sleep(2)
            self.sp.set_firstname(self.firstname)
            self.sp.set_lastname(self.lastname)
            mail_helper = MailHelper()
            temp_email = mail_helper.email
            print("Using email:", temp_email)
            self.sp.set_email(temp_email)
            self.sp.set_phonenumber(self.phonenumber)
            self.sp.set_password(self.password)
            self.sp.set_confirm_password(self.password)
            time.sleep(2)
            self.sp.click_next_button()
            time.sleep(2)
            message = mail_helper.wait_for_email()
            code = mail_helper.get_verification_code(message["id"])
            print("Verification code:", code)

            self.verify.set_verification(code)
            time.sleep(2)
            self.verify.click_verification_button()
            self.agency.set_name(self.name)
            self.agency.set_role(self.role)
            self.agency.set_email(self.agency_email)
            self.agency.set_website(self.website)
            self.agency.set_address(self.address)
            self.agency.click_region_agency()
            time.sleep(2)
            self.agency.set_region_search(self.country)
            time.sleep(2)
            self.agency.click_region_agency()
            time.sleep(2)