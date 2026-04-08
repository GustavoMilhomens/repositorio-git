# 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'

# # importa a classe principal do selenium para interagir com o navegador 
# from selenium import webdriver as wd
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time as tm

# # criar uma instancia do wab drive do chrome 
# driver = wd.Chrome()
# # navega para a url 
# driver.get('https://web.whatsapp.com/')

# # search_box = driver.find_element(By.NAME, 'q')

# # search_box.send_keys('')#"Selenium"

# # search_box.send_keys(Keys.ENTER)
# while True :
#     tm.sleep(1)

import time as tm
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

tm.sleep(5)
title = driver.title

driver.implicitly_wait(0.5)

text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
tm.sleep(15)

text_box.send_keys("Selenium")
tm.sleep(15)# 
submit_button.click()
tm.sleep(15)

message = driver.find_element(by=By.ID, value="message")
text = message.text
tm.sleep(5)

print(text)

driver.quit()
