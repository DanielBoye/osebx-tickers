from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Open browser and navigate to URL
driver = webdriver.Chrome()
driver.get("https://finance.yahoo.com/quote/2020.OL?p=2020.OL&.tsrc=fin-srch")

time.sleep(2)

# Locate the object that contains the number value
# object = driver.find_element_by_xpath("/\//*[@id="quote-header-info"]/div[3]/div[1]/div/fin-streamer[1]")

cookies = driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/div[2]/div[2]/button')
cookies.click()
time.sleep(3)

do_not_save = driver.find_element(By.XPATH, '//*[@id="myLightboxContainer"]/section/button[2]')
do_not_save.click()
time.sleep(3)


object = driver.find_element(By.XPATH, '//*[@id="quote-header-info"]/div[3]/div[1]/div/fin-streamer[1]')
number_value = object.text




# Write the number value to a text file
with open("numberValue.txt", "w") as file:
    file.write(number_value)

# Close the browser
driver.quit()
