from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By


class Test_Sauce:
    def testInvalidLogin(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)

        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(2)

        usernameInput.send_keys("")
        passwordInput.send_keys("")
        sleep(2)
        loginBtn = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginBtn.click()
        errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text =="Epic sadface: Username is required"
        print(f"TEST SONUCU: {testResult}")
        sleep(15)

testClass = Test_Sauce()
testClass.testInvalidLogin()



def testEmptyPassword(self):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    sleep(5)

    usernameInput = driver.find_element(By.ID, "user-name")
    passwordInput = driver.find_element(By.ID, "password")
    sleep(2)

    usernameInput.send_keys("1")
    passwordInput.send_keys("")
    sleep(2)
    loginBtn = driver.find_element(By.ID, "login-button")
    sleep(2)
    loginBtn.click()
    errorMessage = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
    testResult = errorMessage.text == "Epic sadface: Password is required"
    print(f"TEST SONUCU: {testResult}")

testClass = Test_Sauce()
testClass.test
