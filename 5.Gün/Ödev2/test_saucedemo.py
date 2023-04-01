from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path
from datetime import date


class Test_DemoClass:

    # her testten önce çağrılır
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")

        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)



    # her testten sonra çağrılır
    def teardown_method(self):
        self.driver.quit()
    
    # elementin görünür olduğunu kontrol eder
    def waitForElementVisible(self,locator,timeout=10):
        WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))


    # Kullanıcı adı ve şifre alanları boş geçilme durumu
    def test_empty_login(self):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID, "password")
        
        usernameInput.send_keys("")
        passwordInput.send_keys("")
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-empty-login.png")
        assert errorMessage.text =="Epic sadface: Username is required"



    # Sadece şifre alanı boş geçilme durum
    def test_empty_password(self):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID, "password")
        
        usernameInput.send_keys("1")
        passwordInput.send_keys("")
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test_empty-password.png")
        assert errorMessage.text == "Epic sadface: Password is required"



    # Kullanıcı adı kilitli kullanıcı olan durum
    def test_invalid_login(self):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID, "password")
        
        usernameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-invalid-login.png")
        assert errorMessage.text == "Epic sadface: Sorry, this user has been locked out."



    # Hata mesajınaki 'X' butonuna basınca  
    # kullanıcı adı ve şifredeki 'X' butonu kayboması durumu
    def test_icon_login(self):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID, "password")

        usernameInput.send_keys("")
        passwordInput.send_keys("")
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        errorBtn = self.driver.find_element(By.CLASS_NAME, "error-button")
        errorBtn.click()
        self.driver.save_screenshot(f"{self.folderPath}/test-icon-login.png")


    # Geçerli giriş yapıldığındaki durum
    def test_valid_login(self):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID, "password")
        

        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        self.driver.get("https://www.saucedemo.com/inventory.html")
        self.driver.save_screenshot(f"{self.folderPath}/test-valid-login.png")




    
    # Giriş yapıldığında inventory.html sayfasında kullanıcıya gösterilen 
    # ürün sayısı 6 adet olma durumu
    def test_enter_login(self):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID, "password")
        

        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()

        self.driver.get("https://www.saucedemo.com/inventory.html")
        productList = self.driver.find_element(By.ID, "inventory_container")
        productList.click()
        self.driver.save_screenshot(f"{self.folderPath}/test-enter-login.png")





    # Farklı kullanıcılarla geçersiz giriş yapılma durumu (yeni test 1)
    @pytest.mark.parametrize("username,password", [("admin","admin123"), ("Aykut","123"), ("user","123")])
    def test_different_user_login(self,username,password):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID, "password")

        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()

        errorMessage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]")
        self.driver.save_screenshot(f"{self.folderPath}/test-different-user-{username}-{password}.png")
        assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service"





    # Giriş yapıldıktan sonra sepete ürün ekleme durumu (yeni test 2)
    def test_add_product(self):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID, "password")
        

        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        

        addProduct = self.driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']")
        addProduct.click()
        
        self.driver.get("https://www.saucedemo.com/cart.html")
        self.waitForElementVisible((By.CLASS_NAME, "shopping_cart_link"))
        shoppingCart = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        shoppingCart.click()
        self.driver.save_screenshot(f"{self.folderPath}/test-add-product.png")




    # Sepete eklenen ürünün silinmesi durumu (yeni test 3)
    def test_delete_product(self):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID, "password")

        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()

        addProduct = self.driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']")
        addProduct.click()
        
        self.driver.get("https://www.saucedemo.com/cart.html")
        self.waitForElementVisible((By.CLASS_NAME, "shopping_cart_link"))
        shoppingCart = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        shoppingCart.click()


        deleteProduct = self.driver.find_element(By.ID, "remove-sauce-labs-backpack")
        deleteProduct.click()
        self.driver.save_screenshot(f"{self.folderPath}/test-delete-product.png")
        

    




    


        
        




        
        
        