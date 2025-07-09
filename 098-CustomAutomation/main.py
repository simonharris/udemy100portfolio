from selenium import webdriver
from selenium.webdriver.common.by import By


START_PAGE = 'https://musiclivecolchester.com/'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(START_PAGE)



