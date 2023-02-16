# Test Case
#-----------------------------------
# --------
# 1) Open web browser(Chrome/ff/IE).
# 2) Open URL https://admin-demo.nopcommerce.com/login
# 3) Provide Email(admin@yourstore.com)
# 4) Provide password(admin).
# 5) Click on login.
# 6) Capture title of the dashboard page. (Actual title).
# 7) Verify title of the page: Dashborad/ nopcommerce adminstration" (Expected)
# 8) Close Browser

# from selenium import webdriver
#
# from selenium.webdriver.chrome.service import Service
#
# ser_obj = Service("C:/Users/akash.chandel.ACS/Desktop/Drivers/chromedriver.exe")
# driver = webdriver.Chrome(service=ser_obj)
#
# driver.get("https://www.google.co.in/")
#
# driver.maximize_window()
#
# driver.close()


from selenium import  webdriver

driver = webdriver.Chrome(executable_path="C:/Users/akash.chandel.ACS/Desktop/Drivers/chromedriver.exe")

driver.get("https://www.google.co.in/")

driver.maximize_window()

driver.close()
