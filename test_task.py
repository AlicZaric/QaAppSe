"""My homework"""
import random
from time import sleep

import pytest
from selenium import webdriver

from conftest import BaseTest
from constants.base import BaseConstants
from constants.login_page import LoginPageConstants


class TestRegistrationPage(BaseTest):

    @pytest.fixture(scope="function", autouse=True)
    def driver(self):
        driver = webdriver.Chrome(executable_path=BaseConstants.DRIVER_PATH)
        yield driver
        driver.close()

    def test_invalid_login(self, driver):
        # Open start page
        driver.get(BaseConstants.START_PAGE_URL)
        self.log.info("Open page")

        # Clear required fields
        username = driver.find_element_by_xpath(LoginPageConstants.SIGN_IN_USERNAME_XPATH)
        username.clear()
        username.send_keys("Name333")

        password = driver.find_element_by_xpath(LoginPageConstants.SIGN_IN_PASSWORD_XPATH)
        password.clear()
        password.send_keys("Passw234567")
        self.log.info("Fields are filled with invalid values")

        # Click the btn
        sign_in_button = driver.find_element_by_xpath(LoginPageConstants.SIGN_IN_BUTTON_XPATH)
        sign_in_button.click()
        self.log.info("Clicked on button")

        # Check the warning message
        error_message = driver.find_element_by_xpath(LoginPageConstants.INVALID_LOGIN_MESSAGE_XPATH)
        assert error_message.text == LoginPageConstants.INVALID_LOGIN_MESSAGE_TEXT
        self.log.info("vse ok")

    # Тест на пустые значения в окне регистрации
    def test_invalid_reg(self, driver):
        # Open start page
        driver.get(BaseConstants.START_PAGE_URL)
        self.log.info("Open page")

        # Clear required fields
        username = driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_USERNAME_XPATH)
        username.clear()

        mail = driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_EMAIL_XPATH)
        mail.clear()

        password = driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_PASSWORD_XPATH)
        password.clear()
        self.log.info("Fields are filled with invalid values")

        # Click the btn
        sign_in_button = driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_BUTTON_XPATH)
        sign_in_button.click()
        sleep(1)
        self.log.info("Clicked on button")

        # Check the warning message
        error_message = driver.find_elements_by_xpath(LoginPageConstants.INVALID_REG_MESSAGE_XPATH)
        assert len(error_message) == 3
        self.log.info("vse ok")

    # Тест с заполненым полем логина и пустыми полями мейла и пассворда
    def test_invalid_reg_with_login(self, driver):
        valid_login = 'Alisazaric'

        # Open start page
        driver.get(BaseConstants.START_PAGE_URL)
        self.log.info("Open page")

        username = driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_USERNAME_XPATH)
        username.clear()
        username.send_keys(valid_login)

        mail = driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_EMAIL_XPATH)
        mail.clear()

        password = driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_PASSWORD_XPATH)
        password.clear()

        self.log.info("Fields are filled with invalid values")

        # Click the btn
        sign_in_button = driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_BUTTON_XPATH)
        sign_in_button.click()
        self.log.info("Clicked on button")

        error_message_mail = driver.find_element_by_xpath(
            LoginPageConstants.ERROR_MESSAGE_MAIL_XPATH)
        error_message_password = driver.find_element_by_xpath(LoginPageConstants.ERROR_MESSAGE_PASSWORD_XPATH)
        assert error_message_mail.text == LoginPageConstants.ERROR_MESSAGE_MAIL_TEXT
        assert error_message_password.text == LoginPageConstants.ERROR_MESSAGE_PASSWORD_TEXT
        self.log.info("vse ok")

    # Тест с заполненым полем мейла и пустыми полями логина и пассворда
    def test_invalid_reg_with_mail(self, driver):
        valid_mail = 'alisa@gmail.com'

        # Open start page
        driver.get(BaseConstants.START_PAGE_URL)
        self.log.info("Open page")

        username = driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_USERNAME_XPATH)
        username.clear()

        mail = driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_EMAIL_XPATH)
        mail.clear()
        mail.send_keys(valid_mail)

        password = driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_PASSWORD_XPATH)
        password.clear()

        self.log.info("Fields are filled with invalid values")

        # Click the btn
        sign_in_button = driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_BUTTON_XPATH)
        sign_in_button.click()
        self.log.info("Clicked on button")

        error_message_username = driver.find_element_by_xpath(LoginPageConstants.ERROR_MESSAGE_USERNAME_XPATH)
        error_message_password = driver.find_element_by_xpath(LoginPageConstants.ERROR_MESSAGE_PASSWORD_XPATH)
        assert error_message_username.text == LoginPageConstants.ERROR_MESSAGE_USERNAME_TEXT
        assert error_message_password.text == LoginPageConstants.ERROR_MESSAGE_PASSWORD_TEXT
        self.log.info("vse ok")

    def test_invalid_reg_with_pasw(self, driver):
        valid_password = '1234567890okjhgfd#'

        # Open start page
        driver.get(BaseConstants.START_PAGE_URL)
        self.log.info("Open page")

        username = driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_USERNAME_XPATH)
        username.clear()

        mail = driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_EMAIL_XPATH)
        mail.clear()

        password = driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_PASSWORD_XPATH)
        password.clear()
        password.send_keys(valid_password)

        # Click the btn
        sign_in_button = driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_BUTTON_XPATH)
        sign_in_button.click()
        self.log.info("Clicked on button")

        error_message_username = driver.find_element_by_xpath(LoginPageConstants.ERROR_MESSAGE_USERNAME_XPATH)
        error_message_email = driver.find_element_by_xpath(LoginPageConstants.ERROR_MESSAGE_MAIL_XPATH)
        assert error_message_username.text == LoginPageConstants.ERROR_MESSAGE_USERNAME_TEXT
        assert error_message_email.text == LoginPageConstants.ERROR_MESSAGE_MAIL_TEXT
        self.log.info("vse ok")

    # написала тест на регистрацию. Тест прошел, я зарегистрировалась)
    # потом решила дописать асерт, который проверяет, что такой мейл зареген
    def test_valid_reg(self, driver):
        valid_login = 'Alisazaric'
        valid_mail = 'alis.zaric@gmail.com'
        valid_password = '3236107505Ss'

        # Open start page
        driver.get(BaseConstants.START_PAGE_URL)
        self.log.info("Open page")

        username = driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_USERNAME_XPATH)
        username.clear()
        username.send_keys(valid_login)
        sleep(1)

        mail = driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_EMAIL_XPATH)
        mail.clear()
        mail.send_keys(valid_mail)
        sleep(1)

        password = driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_PASSWORD_XPATH)
        password.clear()
        password.send_keys(valid_password)
        sleep(1)

        # Click the btn
        sign_in_button = driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_BUTTON_XPATH)
        sign_in_button.click()
        self.log.info("Clicked on button")

        error_message_mail_used = driver.find_element_by_xpath(LoginPageConstants.ERROR_MESSAGE_MAIL_USED_XPATH)
        assert error_message_mail_used.text == LoginPageConstants.ERROR_MESSAGE_MAIL_USED_TEXT
        self.log.info("vse ok")

    # Тест на успешный логин с проверкой
    def test_valid_login(self, driver):
        valid_login = 'Alisazaric'
        valid_password = '3236107505Ss'

        # Open start page
        driver.get(BaseConstants.START_PAGE_URL)
        self.log.info("Open page")

        # Clear required fields
        username = driver.find_element_by_xpath(LoginPageConstants.SIGN_IN_USERNAME_XPATH)
        username.clear()
        username.send_keys(valid_login)

        password = driver.find_element_by_xpath(LoginPageConstants.SIGN_IN_PASSWORD_XPATH)
        password.clear()
        password.send_keys(valid_password)

        # Click the btn
        sign_in_button = driver.find_element_by_xpath(LoginPageConstants.SIGN_IN_BUTTON_XPATH)
        sign_in_button.click()
        self.log.info("Clicked on button")

        profile_name = driver.find_element_by_xpath(f".//*[contains(text(), '{valid_login.lower()}')]")
        assert profile_name.text == f'{valid_login.lower()}'
        self.log.info("I am here")

    # Тест на логин с рандомными данными
    def test_log_valid(self, driver):
        random_number = random.randint(100, 999)
        valid_login = f"name{random_number}"
        valid_password = f"long_password{random_number}"
        valid_mail = f"mail{random_number}@mail.com"

        # Open start page
        driver.get(BaseConstants.START_PAGE_URL)
        self.log.info("Open page")

        # Clear required fields
        username = driver.find_element_by_xpath(LoginPageConstants.SIGN_IN_USERNAME_XPATH)
        username.clear()
        username.send_keys(valid_login)
        sleep(2)

        password = driver.find_element_by_xpath(LoginPageConstants.SIGN_IN_PASSWORD_XPATH)
        password.clear()
        password.send_keys(valid_password)
        sleep(3)

        # Click the btn
        sign_in_button = driver.find_element_by_xpath(LoginPageConstants.SIGN_IN_BUTTON_XPATH)
        sign_in_button.click()
        self.log.info("Clicked on button")

        error_message = driver.find_element_by_xpath(LoginPageConstants.INVALID_LOGIN_MESSAGE_XPATH)
        assert error_message.text == LoginPageConstants.INVALID_LOGIN_MESSAGE_TEXT
        self.log.info("vse ok")

    # Тест на регистрацию рандомными данными с проверкой
    def test_reg_valid(self, driver):
        random_number = random.randint(100, 999)
        valid_login = f"name{random_number}"
        valid_password = f"long_password{random_number}"
        valid_mail = f"mail{random_number}@mail.com"

        # Open start page
        driver.get(BaseConstants.START_PAGE_URL)
        self.log.info("Open page")

        username = driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_USERNAME_XPATH)
        username.clear()
        username.send_keys(valid_login)
        sleep(1)

        mail = driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_EMAIL_XPATH)
        mail.clear()
        mail.send_keys(valid_mail)
        sleep(1)

        password = driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_PASSWORD_XPATH)
        password.clear()
        password.send_keys(valid_password)
        sleep(1)

        # Click the btn
        sign_in_button = driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_BUTTON_XPATH)
        sign_in_button.click()
        self.log.info("Clicked on button")

        profile_name = driver.find_element_by_xpath(f".//*[contains(text(), 'name{random_number}')]")
        assert profile_name.text == f"name{random_number}"
        self.log.info("I am here")
        self.log.info("Have a nice day")
