from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AgencyPage:
    name_xpath = "//input[@name='agency_name']"
    role_xpath = "//input[@placeholder='Enter Your Role in Agency']"
    email_xpath = "//input[@placeholder='Enter Your Agency Email Address']"
    website_xpath = "//input[@placeholder='Enter Your Agency Website']"
    address_xpath = "//input[@placeholder='Enter Your Agency Address']"
    region_dropdown_xpath = "//button[@role='combobox']"
    region_search_xpath = "//span[@class='font-satoshi-regular text-translucent']"
    region_country_css = "div.flex.cursor-pointer.items-center.justify-between.p-2.space-y-1.hover\\:bg-accent.bg-accent"
    next_button_xpath = "//button[normalize-space()='Next']"

    def __init__(self, driver):
        self.driver = driver

    def set_name(self, name):
        name_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.name_xpath))
        )
        name_field.clear()
        name_field.send_keys(name)

    def set_role(self, role):
        role_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.role_xpath))
        )
        role_field.clear()
        role_field.send_keys(role)

    def set_email(self, agency_email):
        email_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.email_xpath))
        )
        email_field.clear()
        email_field.send_keys(agency_email)

    def set_website(self, website):
        website_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.website_xpath))
        )
        website_field.clear()
        website_field.send_keys(website)

    def set_address(self, address):
        address_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.address_xpath))
        )
        address_field.clear()
        address_field.send_keys(address)

    def click_region_agency(self):
        self.driver.find_element(By.XPATH, self.region_dropdown_xpath).click()

    def set_region_search(self, country):
        search_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.region_search_xpath))
        )

        search_field.send_keys(country)

    def click_region_country(self):
        self.driver.find_element(By.CSS_SELECTOR, self.region_country_css).click()

    def click_next_button(self):
        self.driver.find_element(By.XPATH, self.next_button_xpath).click()
