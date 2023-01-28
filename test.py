from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Open browser and navigate to URL
driver = webdriver.Chrome()
driver.get("https://finance.yahoo.com/quote/AEGA.OL?p=&.tsrc=fin-srch")

driver.implicitly_wait(2)
#maximize browser
driver.maximize_window()
# Locate the object that contains the number value
# object = driver.find_element_by_xpath("/\//*[@id="quote-header-info"]/div[3]/div[1]/div/fin-streamer[1]")

cookies = driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/div[2]/div[2]/button')
print("Found cookies")
cookies.click()
print("Clicked cookies")
driver.implicitly_wait(2)

do_not_save = driver.find_element(By.XPATH, '//*[@id="myLightboxContainer"]/section/button[2]')
print("Found no")
do_not_save.click()
print("Clicked no")
driver.implicitly_wait(2)


object = driver.find_element(By.XPATH, '//*[@id="quote-header-info"]/div[3]/div[1]/div/fin-streamer[1]')
number_value = object.text




# Write the number value to a text file
with open("numberValue.txt", "w") as file:
    file.write(number_value)

# Close the browser
driver.quit()
