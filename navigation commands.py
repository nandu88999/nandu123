from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path="C:\\Users\\admin\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.youtube.com/")
time.sleep(5)
print(driver.title)
driver.get("https://www.amazon.in/")
print(driver.title)
time.sleep(5)
driver.back()
print(driver.title)
time.sleep(5)
driver.forward()
print(driver.title)
time.sleep(5)
driver.close()
#this navigating commands use when we open multiple websites in same page we well use this commands to navigate 