from tests.base_test import BaseTest
from config import *
from selenium.webdriver.common.keys import Keys
from utils.test_data_generator import *
import sys
import time
from selenium.webdriver.support import expected_conditions as EC


class Test(BaseTest):
    def __init__(self, driver, base_url, module):
        super(Test, self).__init__(driver, base_url, module)

    def run(self):
        # UI fields tests
        self.verify_terms_of_use_link_on_signup()
        self.verify_signup_page_load()
        self.verify_all_labels()
        self.verify_all_field_exists()
        self.verify_field_username_validations()
        self.verify_field_password_validations()
        self.verify_field_email_validations()

        # submit tests
        self.verify_invalid_signup_on_submit()
        self.verify_valid_signup_with_all_fields()
        self.verify_valid_signup_with_mandatory_fields()
        self.verify_unique_username_signup()
        self.verify_signup_with_enter()

    def verify_signup_page_load(self):
        self.start_log(sys._getframe().f_code.co_name)
        self.load_page()
        if self.driver.title == signup_page_title:
            self.passed('SignUp Page loaded successfully')
        else:
            self.failed('SignUp Page load failed')
        self.end_log(sys._getframe().f_code.co_name)

    def verify_valid_signup_with_all_fields(self):
        self.start_log(sys._getframe().f_code.co_name)
        self.load_page()

        # get elements
        username_field = self.get_element_by_id(username_id)
        password_field = self.get_element_by_id(password_id)
        email_field = self.get_element_by_id(email_id)
        first_name_field = self.get_element_by_id(first_name_id)
        last_name_field = self.get_element_by_id(last_name_id)
        submit_form = self.get_element_by_id(signup_submit_id)

        # send data
        username_field.send_keys(get_user_name())
        password_field.send_keys(get_password())
        email_field.send_keys(get_email())
        first_name_field.send_keys(get_first_name())
        last_name_field.send_keys(get_last_name())

        submit_form.click()


        self.verify_label('Welcome')
        self.sign_out()
        self.end_log(sys._getframe().f_code.co_name)

    def verify_valid_signup_with_mandatory_fields(self):
        self.start_log(sys._getframe().f_code.co_name)
        self.load_page()

        username_field = self.get_element_by_id(username_id)
        password_field = self.get_element_by_id(password_id)
        email_field = self.get_element_by_id(email_id)
        submit_form = self.get_element_by_id(signup_submit_id)

        # send data
        username_field.send_keys(get_user_name())
        password_field.send_keys(get_password())
        email_field.send_keys(get_email())

        submit_form.click()

        self.verify_label('Welcome')
        self.sign_out()
        self.end_log(sys._getframe().f_code.co_name)

    def verify_unique_username_signup(self):
        self.start_log(sys._getframe().f_code.co_name)

        self.load_page()

        # get elements
        username_field = self.get_element_by_id(username_id)
        password_field = self.get_element_by_id(password_id)
        email_field = self.get_element_by_id(email_id)
        submit_form = self.get_element_by_id(signup_submit_id)

        # send data
        existing_username = get_user_name()
        username_field.send_keys(existing_username)
        password_field.send_keys(get_password())
        email_field.send_keys(get_email())

        submit_form.click()

        # sign out
        self.sign_out()

        self.load_page()
        username_field = self.get_element_by_id(username_id)
        username_field.clear()
        username_field.send_keys(existing_username)
        username_field.send_keys(Keys.TAB)

        self.verify_error(password_error_for_minimum_characters)
        self.end_log(sys._getframe().f_code.co_name)

    def verify_signup_with_enter(self):
        self.start_log(sys._getframe().f_code.co_name)

        username_field = self.get_element_by_id(username_id)
        password_field = self.get_element_by_id(password_id)
        email_field = self.get_element_by_id(email_id)
        submit_form = self.get_element_by_id(signup_submit_id)
        last_name_field = self.get_element_by_id(last_name_id)

        # send data
        username_field.send_keys(get_user_name())
        password_field.send_keys(get_password())
        email_field.send_keys(get_email())

        last_name_field.send_keys(Keys.TAB)

        submit_form.send_keys(Keys.ENTER)

        self.verify_label('Welcome')
        self.sign_out()
        self.end_log(sys._getframe().f_code.co_name)

    def verify_invalid_signup_on_submit(self):
        self.start_log(sys._getframe().f_code.co_name)

        self.load_page()
        # get elements
        username_field = self.get_element_by_id(username_id)
        password_field = self.get_element_by_id(password_id)
        email_field = self.get_element_by_id(email_id)
        first_name_field = self.get_element_by_id(first_name_id)
        last_name_field = self.get_element_by_id(last_name_id)
        submit_form = self.get_element_by_id(signup_submit_id)

        # send data
        username_field.send_keys('Keerthi Banala')
        password_field.send_keys('abcd')
        email_field.send_keys(get_email())
        first_name_field.send_keys(get_first_name())
        last_name_field.send_keys(get_last_name())

        submit_form.click()

        if self.driver.find_element_by_class_name('ErrorMessage'):
            self.passed('Valid error message class on invalid signup')
        else:
            self.failed('Invalid error message class on invalid signup')

        self.end_log(sys._getframe().f_code.co_name)

    def verify_all_labels(self):
        self.start_log(sys._getframe().f_code.co_name)

        self.load_page()
        self.verify_label(username_label)
        self.verify_label(password_label)
        self.verify_label(email_label)
        self.verify_label(first_name_label)
        self.verify_label(last_name_label)
        self.end_log(sys._getframe().f_code.co_name)

    def verify_all_field_exists(self):
        self.start_log(sys._getframe().f_code.co_name)
        self.load_page()
        self.verify_field_exists(username_id)
        self.verify_field_exists(password_id)
        self.verify_field_exists(email_id)
        self.verify_field_exists(first_name_id)
        self.verify_field_exists(last_name_id)
        self.verify_field_exists(signup_submit_id)
        self.end_log(sys._getframe().f_code.co_name)


    def verify_field_username_validations(self):
        self.start_log(sys._getframe().f_code.co_name)
        self.load_page()
        username_field = self.get_element_by_id(username_id)
        username_sample = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa' # 50 characters
        username_sample = username_sample + username_sample # 100 characters
        username_field.clear()
        username_field.send_keys(username_sample)
        username_field_value = self.get_field_value(username_field)

        if len(username_field_value) == 50:
            self.passed('Username can only be 50 characters, removed additional characters.')
        else:
            self.failed('Username can only be 50 characters, did not remove additional characters properly.')

        username_sample = 'ab    c'
        username_field.clear()
        username_field.send_keys(username_sample)
        username_field.send_keys(Keys.TAB)

        self.verify_error(username_error_for_spaces)

        # tab to next field without entering details
        username_field.clear()
        username_field.send_keys(Keys.TAB)
        self.verify_error(username_mandatory_error)
        self.end_log(sys._getframe().f_code.co_name)

    def verify_field_password_validations(self):
        self.start_log(sys._getframe().f_code.co_name)
        self.load_page()
        password_field = self.get_element_by_id(password_id)

        # Minimum characters validation
        password_sample = 'aaaa'  # 4 characters
        password_field.clear()
        password_field.send_keys(password_sample)
        password_field.send_keys(Keys.TAB)
        self.verify_error(password_error_for_minimum_characters)

        # Common password validation
        password_sample = '12345678'  # common password
        password_field.clear()
        password_field.send_keys(password_sample)
        password_field.send_keys(Keys.TAB)
        self.verify_error(password_error_for_common_password)

        # verify if is a password type field
        if password_field.get_attribute('type') == 'password':
            self.passed('Yes, it is a password type field')
        else:
            self.failed('No, it is not a password type field')

        # tab to next field without entering details
        password_field.clear()
        password_field.send_keys(Keys.TAB)
        self.verify_error(password_mandatory_error)
        self.end_log(sys._getframe().f_code.co_name)

    def verify_field_email_validations(self):
        self.start_log(sys._getframe().f_code.co_name)
        self.load_page()
        email_field = self.get_element_by_id(email_id)

        # invalid email format validation
        email_sample = 'blah'
        email_field.clear()
        email_field.send_keys(email_sample)
        email_field.send_keys(Keys.TAB)
        self.verify_error(email_error_for_invalid_email_format)

        email_sample = 'blah@blah'
        email_field.clear()
        email_field.send_keys(email_sample)
        email_field.send_keys(Keys.TAB)
        self.verify_error(email_error_for_invalid_email_format)

        email_sample = 'blah.com'
        email_field.clear()
        email_field.send_keys(email_sample)
        email_field.send_keys(Keys.TAB)
        self.verify_error(email_error_for_invalid_email_format)

        email_sample = '123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123401@gmail.com1234'
        expected_email_after_trim = '123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123401@gmail.com'
        email_field.clear()
        email_field.send_keys(email_sample)
        email_field.send_keys(Keys.TAB)
        actual_email_sample = self.get_field_value(email_field)

        if actual_email_sample == expected_email_after_trim:
            self.passed('Email can only be 250 characters, removed additional characters.')
        else:
            self.failed('Email can only be 250 characters, did not remove additional characters properly.')

        # tab to next field without entering details
        email_field.clear()
        email_field.send_keys(Keys.TAB)
        self.verify_error(email_mandatory_error)
        self.end_log(sys._getframe().f_code.co_name)

    def verify_terms_of_use_link_on_signup(self):
        self.start_log(sys._getframe().f_code.co_name)
        self.load_page()

        main_window = self.driver.current_window_handle

        terms_use_link = self.get_element_by_link_text('Terms of Use')
        terms_use_link.click()
        self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)

        self.driver.switch_to_window(self.get_window())

        time.sleep(5)
        self.wait.until(EC.presence_of_all_elements_located)
        print(self.driver.title)
        if self.driver.title == terms_of_use_title:
            self.passed('Terms of use page is loaded')
        else:
            self.failed('Terms of use page is NOT loaded')

        self.driver.close()

        self.driver.switch_to_window(main_window)
        privacy_policy_link = self.get_element_by_link_text('Privacy Policy')
        privacy_policy_link.click()

        self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
        self.driver.switch_to_window(self.get_window())

        time.sleep(5)
        self.wait.until(EC.presence_of_all_elements_located)
        print(self.driver.title)
        if self.driver.title == privacy_policy_title:
            self.passed('privacy_policy_title is loaded')
        else:
            self.failed('privacy_policy_title is NOT loaded')

        self.driver.close()

        self.driver.switch_to_window(main_window)

        self.end_log(sys._getframe().f_code.co_name)


