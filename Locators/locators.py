class Locators():

    # Login Page Objects
    username_textbox_xpath = "//input[@name='username']"
    password_textbox_xpath = "//input[@name='password']"
    login_button_xpath = "//button[@type='submit']"
    invalidCredentials_message_xpath = "//p[text()='Invalid credentials']"

    # Home Page Objects
    user_dropdown_xpath = "//span[@class='oxd-userdropdown-tab']/i"
    logout_link_xpath = "//ul[@class='oxd-dropdown-menu']//li/a[contains(text(),'Logout')]"