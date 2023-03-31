from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By


class Test_Sauce:

    # Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak 
    # "Epic sadface: Username is required" gösterilmelidir.

    def testEmptyLogin(self):
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





    # Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak 
    # "Epic sadface: Password is required" gösterilmelidir.
    
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
        sleep(20)



    
    # Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde 
    # "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.

    def testInvalidLogin(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)

        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(2)

        usernameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginBtn = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginBtn.click()
        errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"TEST SONUCU: {testResult}")
        sleep(20)
    


    
    # Kullanıcı adı ve şifre alanları boş geçildiğinde bu iki inputun yanında da kırmızı "X" ikonu çıkmalıdır.
    # Daha sonra aşağıda çıkan uyarı mesajının kapatma butonuna tıklandığında 
    # bu "X" ikonları kaybolmalıdır. (Tek test casede işleyiniz)

    def testIconLogin(self):
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

        errorBtn = driver.find_element(By.CLASS_NAME, "error-button")
        sleep(10)
        errorBtn.click()
        sleep(5)



    
    # Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde 
    # kullanıcı "/inventory.html" sayfasına gönderilmelidir.


    def testValidLogin(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)

        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(2)

        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginBtn = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginBtn.click()

        driver.maximize_window()
        driver.get("https://www.saucedemo.com/inventory.html")
        sleep(20)




    # Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.

    def testEnterLogin(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)

        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(2)

        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginBtn = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginBtn.click()

        driver.maximize_window()
        driver.get("https://www.saucedemo.com/inventory.html")
        sleep(15)

        productList = driver.find_element(By.ID, "inventory_container")
        sleep(5)
        productList.click()
        sleep(10)





testClass = Test_Sauce() 
testClass.testEmptyLogin() # 1.fonksiyon


testClass = Test_Sauce()
testClass.testEmptyPassword() # 2.fonksiyon


testClass = Test_Sauce()
testClass.testInvalidLogin() # 3.fonksiyon


testClass = Test_Sauce()
testClass.testIconLogin() # 4.fonksiyon
sleep(25)


testClass = Test_Sauce()
testClass.testValidLogin() # 5.fonksiyon
sleep(10)


testClass = Test_Sauce()
testClass.testEnterLogin() # 6.fonksiyon
sleep(20)
