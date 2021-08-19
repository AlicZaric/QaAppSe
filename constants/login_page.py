class LoginPageConstants:
    """Store constants related to Login Page"""
    SIGN_UP_USERNAME_XPATH = ".//input[@id='username-register']"
    SIGN_UP_EMAIL_XPATH = ".//input[@id='email-register']"
    SIGN_UP_PASSWORD_XPATH = ".//input[@id='password-register']"
    SIGN_UP_BUTTON_XPATH = ".//button[@type='submit']"
    SIGN_UP_BUTTON_TEXT = 'Sign up'

    # Sign in
    SIGN_IN_USERNAME_XPATH = ".//input[@placeholder='Username']"
    SIGN_IN_PASSWORD_XPATH = ".//input[@placeholder='Password']"
    SIGN_IN_BUTTON_TEXT = 'Sign In'

    # Messages
    INVALID_LOGIN_MESSAGE_TEXT = 'Invalid username / password'
    INVALID_REG_MESSAGE_XPATH = ".//div[@class='alert alert-danger small liveValidateMessage liveValidateMessage--visible']"
    ERROR_MESSAGE_MAIL_TEXT = 'You must provide a valid email address.'
    ERROR_MESSAGE_MAIL_XPATH = ".//div[contains(text(), 'You must provide a valid email address')]"
    ERROR_MESSAGE_PASSWORD_TEXT = 'Password must be at least 12 characters.'
    ERROR_MESSAGE_PASSWORD_XPATH = ".//div[contains(text(), 'Password must be at least 12 characters')]"
    ERROR_MESSAGE_USERNAME_TEXT = 'Username must be at least 3 characters.'
    ERROR_MESSAGE_USERNAME_XPATH = ".//div[contains(text(), 'Username must be at least 3 characters.')]"
    ERROR_MESSAGE_MAIL_USED_TEXT = 'That email is already being used.'
    ERROR_MESSAGE_MAIL_USED_XPATH = ".//div[contains(text(), 'That email is already being used.')]"
