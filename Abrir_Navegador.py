from selenium.webdriver import Edge

driver = Edge()
driver.get('https://websalud.minsa.gob.pe/hisminsa/')
driver.maximize_window()
driver.quit()

""" from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions

options = EdgeOptions()
driver = webdriver.Edge(options=options)
driver.get('https://websalud.minsa.gob.pe/hisminsa/')
driver.maximize_window()
driver.quit() """