from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.maximize_window()
driver.get('https://google.com.pe')
assert driver.title # => "Google"

driver.implicitly_wait(0.5)

search_box = driver.find_element(by=By.NAME, value="q")
search_button = driver.find_element(by=By.NAME, value="btnK")

search_box.send_keys("Selenium IDE")
search_button.click()

assert driver.find_element(by=By.NAME, value="q").get_attribute("value") # => "Selenium IDE"
#driver.quit()