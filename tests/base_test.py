from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class BaseTest(object):
    def __init__(self, driver, base_url, module):
        self.driver = driver
        self.base_url = base_url
        self.module = module
        self.wait = WebDriverWait(driver, 10)

    def failed(self, error_message):
        print('Failed: ' + self.module + ':' + error_message)
        self.driver.quit()
        exit()

    def passed(self, success_message):
        print('Passed: ' + success_message)

    def load_page(self):
        self.driver.get(self.base_url)
        # self.driver.maximize_window()
        self.wait.until(EC.presence_of_all_elements_located)

    def get_title(self):
        return self.driver.title

    def get_element_by_link_text(self, link_text):
        return self.driver.find_element_by_link_text(link_text)

    def get_element_by_id(self, element_name):

        return self.driver.find_element_by_id(element_name)

    def get_field_value(self, field):
        return field.get_attribute('value')

    def verify_label(self, expected_label):
        self.wait.until(EC.presence_of_all_elements_located)
        if expected_label in self.driver.page_source:
            self.passed('Valid ' + expected_label + ' label')
        else:
            self.failed('Invalid ' + expected_label + ' label')

    def verify_error(self, error):
        self.wait.until(EC.presence_of_all_elements_located)
        if error in self.driver.page_source:
            self.passed('Valid expected error:' + error)
        else:
            self.failed('Invalid expected error: ' + error)

    def verify_field_exists(self, field_id):
        self.wait.until(EC.presence_of_all_elements_located)
        if self.driver.find_element_by_id(field_id):
            self.passed('Field:' + field_id + ' exists')
        else:
            self.failed('Field:' + field_id + ' does not exist')

    def sign_out(self):
        self.driver.find_element_by_xpath('//*[@id="userAcctTab_MainMenu"]').click()
        self.driver.find_element_by_xpath('//*[@id="dd-my-account"]/ul/li[5]/a').click()

    def start_log(self, function_name):
        print(function_name + ' -> Started')

    def end_log(self, function_name):
        print(function_name + ' -> Ended')

    def keep_trying(self, callback, attempts=60, fallback=None, unsatisfactory=None):
        for i in range(attempts):
            try:
                result = callback()
                if result is not unsatisfactory:
                    return result
            except:
                pass
            time.sleep(3)

        return fallback

    def switch_tab(self, title):
        for handle in self.driver.window_handles:
            self.driver.switch_to_window(handle)
            time.sleep(2)
            if self.driver.title == title:
                break

    def get_window(self):
        current_window = self.driver.current_window_handle

        for handle in self.driver.window_handles:
            if handle != current_window:
                return handle


