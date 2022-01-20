from sys import maxsize
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
options = Options()
options.headless = True
options.__sizeof__()=maxsize
driver = webdriver.Firefox(options=options)