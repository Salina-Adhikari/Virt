import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
class Experience:
    experience_dropdown_xpath="//button[@role='combobox']"
    experience_search_xpath="//select"
    students_recurit_xpath="//input[@placeholder='Enter an approximate number.']"
    focus_area_xpath="//input[@placeholder='E.g., Undergraduate admissions to Canada.']"
    success_xpath="//input[@placeholder='E.g., 90% ']"
    services_counselling_xpath="//button[@role='checkbox' and @value='on']"
    next_button_xpath="//button[normalize-space()='Next']"

    def __init__(self, driver):
        self.driver = driver
    def click_experience(self):
        experience_button=WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.experience_dropdown_xpath))
        )
        experience_button.click()
    def set_experience(self):
        # xpath=self.experience_search_xpath.format(year=year)
        # result=WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, xpath))
        # )
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", result)
        # action=ActionChains(self.driver)
        # action.move_to_element(result).click().perform()
        # time.sleep(2)
        # action.move_to_element(result).click().perform()
        select_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//select"))
        )
        dropdown = Select(select_element)
        dropdown.select_by_visible_text("3 years")

    def set_students(self,number):
        students_field=WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.students_recurit_xpath))
        )
        students_field.send_keys(number)
    def set_focus(self,area):
        focus_field=WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.focus_area_xpath))
        )
        focus_field.send_keys(area)
    def set_success(self,metrics):
        success_field=WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.success_xpath))
        )
        success_field.send_keys(metrics)


    def set_test(self):
        self.driver.find_element(By.XPATH, self.services_counselling_xpath).click()

    def click_next_button(self):
        self.driver.find_element(By.XPATH, self.next_button_xpath).click()











