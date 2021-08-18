"""My homework"""
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from conftest import BaseTest
from constants.base import BaseConstants
from constants.login_page import LoginPageConstants
from constants.profile_page import ProfilePage
from helpers.base import BaseHelpers


class TestRegistrationPage(BaseTest):

    @pytest.fixture(scope="function", autouse=True)
    def driver(self):
        driver = webdriver.Chrome(executable_path=BaseConstants.DRIVER_PATH)
        yield driver
        driver.close()

    def test_invalid_login(self, driver):
        base_helper = BaseHelpers(driver)
        # Open start page
        driver.get(BaseConstants.START_PAGE_URL)
        self.log.info("Open page")

        # Clear and fill required fields
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_IN_USERNAME_XPATH, value="Name333")
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_IN_PASSWORD_XPATH,
                                     value="Passw234567")
        self.log.info("Fields are filled with invalid values")

        # Click the btn
        base_helper.find_by_contains_text(text=LoginPageConstants.SIGN_IN_BUTTON_TEXT, element_tag='button').click()
        self.log.info("Clicked on button")

        # Check the warning message
        error_message = base_helper.find_by_contains_text(LoginPageConstants.INVALID_LOGIN_MESSAGE_TEXT)
        assert error_message.text == LoginPageConstants.INVALID_LOGIN_MESSAGE_TEXT
        self.log.info("vse ok")

    # Тест на пустые значения в окне регистрации
    def test_invalid_reg(self, driver):
        base_helper = BaseHelpers(driver)
        # Open start page
        driver.get(BaseConstants.START_PAGE_URL)
        self.log.info("Open page")

        # Clear and fill required fields
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_USERNAME_XPATH, value='')
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_EMAIL_XPATH, value='')
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_PASSWORD_XPATH, value='')
        self.log.info("Fields are filled with invalid values")

        # Click the btn
        base_helper.find_by_contains_text(text=LoginPageConstants.SIGN_UP_BUTTON_TEXT, element_tag='button').click()
        sleep(1)
        self.log.info("Clicked on button")

        # Check the warning message
        error_message = driver.find_elements_by_xpath(LoginPageConstants.INVALID_REG_MESSAGE_XPATH)
        assert len(error_message) == 3
        self.log.info("vse ok")

    # Тест с заполненым полем логина и пустыми полями мейла и пассворда
    def test_invalid_reg_with_login(self, driver):
        valid_login = 'Alisazaric'
        base_helper = BaseHelpers(driver)

        # Open start page
        driver.get(BaseConstants.START_PAGE_URL)
        self.log.info("Open page")

        # Clear and fill required fields
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_USERNAME_XPATH, value=valid_login)
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_EMAIL_XPATH, value='')
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_PASSWORD_XPATH, value='')
        self.log.info("Fields are filled with invalid values")

        # Click the btn
        base_helper.find_by_contains_text(text=LoginPageConstants.SIGN_UP_BUTTON_TEXT, element_tag='button').click()
        self.log.info("Clicked on button")

        error_message_mail = driver.find_element_by_xpath(LoginPageConstants.ERROR_MESSAGE_MAIL_XPATH)
        error_message_password = driver.find_element_by_xpath(LoginPageConstants.ERROR_MESSAGE_PASSWORD_XPATH)
        assert error_message_mail.text == LoginPageConstants.ERROR_MESSAGE_MAIL_TEXT
        assert error_message_password.text == LoginPageConstants.ERROR_MESSAGE_PASSWORD_TEXT
        self.log.info("vse ok")

    # Тест с заполненым полем мейла и пустыми полями логина и пассворда
    def test_invalid_reg_with_mail(self, driver):
        valid_mail = 'alisa@gmail.com'
        base_helper = BaseHelpers(driver)

        # Open start page
        driver.get(BaseConstants.START_PAGE_URL)
        self.log.info("Open page")

        # Clear and fill required fields
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_USERNAME_XPATH, value='')
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_EMAIL_XPATH, value=valid_mail)
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_PASSWORD_XPATH, value='')
        self.log.info("Fields are filled with invalid values")

        # Click the btn
        base_helper.find_by_contains_text(text=LoginPageConstants.SIGN_UP_BUTTON_TEXT, element_tag='button').click()
        self.log.info("Clicked on button")

        error_message_username = driver.find_element_by_xpath(LoginPageConstants.ERROR_MESSAGE_USERNAME_XPATH)
        error_message_password = driver.find_element_by_xpath(LoginPageConstants.ERROR_MESSAGE_PASSWORD_XPATH)
        assert error_message_username.text == LoginPageConstants.ERROR_MESSAGE_USERNAME_TEXT
        assert error_message_password.text == LoginPageConstants.ERROR_MESSAGE_PASSWORD_TEXT
        self.log.info("vse ok")

    def test_invalid_reg_with_pasw(self, driver):
        valid_password = '1234567890okjhgfd#'
        base_helper = BaseHelpers(driver)

        # Open start page
        driver.get(BaseConstants.START_PAGE_URL)
        self.log.info("Open page")

        # Clear and fill required fields
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_USERNAME_XPATH, value='')
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_EMAIL_XPATH, value='')
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_PASSWORD_XPATH,
                                     value=valid_password)

        # Click the btn
        base_helper.find_by_contains_text(text=LoginPageConstants.SIGN_UP_BUTTON_TEXT, element_tag='button').click()
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
        base_helper = BaseHelpers(driver)

        # Open start page
        driver.get(BaseConstants.START_PAGE_URL)
        self.log.info("Open page")

        # Clear and fill required fields
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_USERNAME_XPATH, value=valid_login)
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_EMAIL_XPATH, value=valid_mail)
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_PASSWORD_XPATH,
                                     value=valid_password)
        sleep(1)

        # Click the btn
        base_helper.find_by_contains_text(text=LoginPageConstants.SIGN_UP_BUTTON_TEXT, element_tag='button').click()
        self.log.info("Clicked on button")

        error_message_mail_used = driver.find_element_by_xpath(LoginPageConstants.ERROR_MESSAGE_MAIL_USED_XPATH)
        assert error_message_mail_used.text == LoginPageConstants.ERROR_MESSAGE_MAIL_USED_TEXT
        self.log.info("vse ok")

    # Тест на успешный логин с проверкой
    def test_valid_login(self, driver):
        valid_login = 'Alisazaric'
        valid_password = '3236107505Ss'
        base_helper = BaseHelpers(driver)

        # Open start page
        driver.get(BaseConstants.START_PAGE_URL)
        self.log.info("Open page")

        # Clear and fill required fields
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_IN_USERNAME_XPATH, value=valid_login)
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_IN_PASSWORD_XPATH,
                                     value=valid_password)

        # Click the btn
        base_helper.find_by_contains_text(text=LoginPageConstants.SIGN_IN_BUTTON_TEXT, element_tag='button').click()
        self.log.info("Clicked on button")

        profile_name = driver.find_element_by_xpath(f".//*[contains(text(), '{valid_login.lower()}')]")
        assert profile_name.text == f'{valid_login.lower()}'
        self.log.info("I am here")

    # Тест на логин с рандомными данными
    def test_log_invalid(self, driver):
        invalid_login = f"name{self.variety}"
        invalid_password = f"long_password{self.variety}"
        base_helper = BaseHelpers(driver)

        # Open start page
        driver.get(BaseConstants.START_PAGE_URL)
        self.log.info("Open page")

        # Clear required fields
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_IN_USERNAME_XPATH,
                                     value=invalid_login)
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_IN_PASSWORD_XPATH,
                                     value=invalid_password)

        # Click the btn
        base_helper.find_by_contains_text(text=LoginPageConstants.SIGN_IN_BUTTON_TEXT, element_tag='button').click()
        self.log.info("Clicked on button")

        error_message = base_helper.find_by_contains_text(LoginPageConstants.INVALID_LOGIN_MESSAGE_TEXT)
        assert error_message.text == LoginPageConstants.INVALID_LOGIN_MESSAGE_TEXT
        self.log.info("vse ok")

    # Тест на регистрацию рандомными данными с проверкой
    def test_register(self, driver):
        valid_login = f"name{self.variety}"
        valid_password = f"long_password{self.variety}"
        valid_mail = f"mail{self.variety}@mail.com"

        base_helper = BaseHelpers(driver)

        # Open start page
        driver.get(BaseConstants.START_PAGE_URL)
        self.log.info("Open page")

        # Fill required fields
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_USERNAME_XPATH, value=valid_login)
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_EMAIL_XPATH, value=valid_mail)
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_PASSWORD_XPATH,
                                     value=valid_password)
        sleep(1)

        # Click the btn
        base_helper.find_by_contains_text(text=LoginPageConstants.SIGN_UP_BUTTON_TEXT, element_tag='button').click()
        self.log.info("Clicked on button")

        hello_message = driver.find_element_by_xpath(ProfilePage.HELLO_MESSAGE_XPATH)
        assert valid_login.lower() in hello_message.text
        assert hello_message.text == f"Hello {valid_login.lower()}, your feed is empty."
        self.log.info("I am here")
