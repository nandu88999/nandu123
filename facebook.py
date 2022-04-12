from selenium import webdriver
driver=webdriver.Chrome(executable_path="C:\\Users\\admin\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.facebook.com/")
nan_username=driver.find_element_by_name("email")
print(nan_username.is_displayed())
print(nan_username.is_enabled())
nan_password=driver.find_element_by_name("pass")
print(nan_password.is_displayed())
print(nan_password.is_enabled())
nan_username.send_keys("nandak551@gmail.com")
nan_password.send_keys("forest@9900")
driver.find_element_by_name("login").click()











