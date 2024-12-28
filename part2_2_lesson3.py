from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 

url = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(url)
    
    num1 = browser.find_element(By.ID, "num1")    
    num2 = browser.find_element(By.ID, "num2")
    value1 = num1.text    
    value2 = num2.text
    total = int(value1) + int(value2)    
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(total))  
    button1 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button1.click()    

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
