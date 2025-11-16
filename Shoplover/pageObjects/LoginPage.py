from selenium.webdriver.common.by import By
class LoginPage():
    def __init__(self, driver):
        self.driver = driver

    email = (By.XPATH, "//input[@id=':r0:']")
    password = (By.XPATH,"//input[@placeholder='Password']")
    logInButton = (By.XPATH,"//button[normalize-space()='Sign In']")
    myOrders = (By.CSS_SELECTOR, "img[class='w-[22px]']")

    def getEmail(self):
        return self.driver.find_element(*LoginPage.email)
    def getPassword(self):
        return self.driver.find_element(*LoginPage.password)

    def getLogInButton(self):
        return self.driver.find_element(*LoginPage.logInButton)
    def getMyOrder(self):
        return self.driver.find_element(*LoginPage.myOrders)

