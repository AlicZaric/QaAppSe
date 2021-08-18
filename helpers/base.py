class BaseHelpers:
    """Store base helpers for Web testing"""

    def __init__(self, driver):
        self.driver = driver

    def fill_input_field(self, by, locator, value):
        """Find required element using by.X model, clear input field and enter the value"""
        username = self.driver.find_element(by=by, value=locator)
        username.clear()
        username.send_keys(value)

    def find_by_contains_text(self, text, element_tag='*'):
        """Find element using XPATH contains function by text"""
        return self.driver.find_element_by_xpath(f".//{element_tag}[contains(text(), '{text}')]")
