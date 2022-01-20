from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.page_load_strategy = 'normal'
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://web.whatsapp.com/")
#driver.quit()