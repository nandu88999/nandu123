from selenium import webdriver
driver=webdriver.Chrome(executable_path="C:/Users/admin/chromedriver_win32/chromedriver.exe")
driver.get("https://www.google.com")
driver.find_element_by_css_selector("div.L3eUgb:nth-child(2) div.o3j99.ikrT4e.om7nvf:nth-child(3) div.A8SBwf.emcav:nth-child(1) div.RNNXgb:nth-child(3) div.SDkEP div.a4bIc > input.gLFyf.gsfi:nth-child(3)").send_keys("bbb")
