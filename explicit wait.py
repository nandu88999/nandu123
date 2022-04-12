from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path="C:\\Users\\admin\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.cheapoair.com/flights/booknow/cheap-flight-tickets?fpaffiliate=coa-google-competitor&fpsub=&utm_campaign=competitors_exact_atlas_global&utm_term=www%20expedia%20com%20flights&utm_term_id=kwd-299032035115&utm_source={google}&utm_medium={cpc}&device=c&fpprice=&campaignID=16272619390&adgroupId=138799178852&gclid=EAIaIQobChMI-fbuyZ389gIVw9CWCh3CEAo1EAAYASAAEgJFjPD_BwE")
driver.find_element(By.ID,"from0").send_keys("hyderabad")
driver.find_element(By.ID,"to0").send_keys("goa")
driver.find_element(By.ID,"cal0").send_keys("12/06/2022")
driver.find_element(By.ID,"cal1").send_keys("14/06/2022")
driver.find_element(By.ID,"travellerButton").click()
driver.find_element(By.ID,"lbladults").send_keys("1")
driver.find_element(By.ID,"Class").send_keys("First")
driver.find_element(By.ID,"closeDialog").click()
driver.find_element(By.ID,"searchNow").click()








