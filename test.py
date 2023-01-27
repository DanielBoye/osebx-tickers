from selenium import webdriver

# Open browser and navigate to URL
driver = webdriver.Chrome()
driver.get("https://www.example.com")

# Locate the object that contains the number value
object = driver.find_element_by_xpath("//*[@id='exampleNumber']")
number_value = object.text

# Write the number value to a text file
with open("numberValue.txt", "w") as file:
    file.write(number_value)

# Close the browser
driver.quit()
