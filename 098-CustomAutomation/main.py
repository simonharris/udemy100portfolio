import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


checks = {
    'apache': False,
    'elasticsearch': False,
    'neo4j': False,
    # '': False,
    # '': False,
    # '': False,

}


START_PAGE = 'https://musiclivecolchester.com/'


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

# load home page
driver.get(START_PAGE)
checks['apache'] = True

# submit search
sb = driver.find_element(By.NAME, "q")
sb.send_keys('Reynolds')
sb.send_keys(Keys.ENTER)


# stalk Reynolds a little more closely
checkbox = driver.find_element(By.ID, "id_models_0")
checkbox.click()

submit = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "adv_search"))
)
submit.click()


link_jim = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Jim Reynolds"))
)
link_jim.click()
checks['elasticsearch'] = True


link_llc = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "The Lamplight Club"))
)
link_llc.click()
checks['neo4j'] = True

print(checks)

